import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from datetime import datetime
import logging
import os
import uuid
import pytest
from playwright.sync_api import Page

from pages.login_page import Login
from pages.product_page import Products
from pages.cart_page import Cart
from pages.checkout_step_one_page import CheckoutOne
from pages.checkout_step_two_page import CheckoutTwo
from pages.complete_page import Complete
from test_data.users import User


@pytest.fixture
def logger():
    return logging.getLogger(__name__)


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    reports_dir = Path(__file__).parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
    report = reports_dir / f"Test_report_{timestamp}.html"
    logging.debug("Creating test report: %s", report)
    config.option.htmlpath = str(report)
    config.option.self_contained_html = True


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    img_path = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    working_root = Path().resolve()
    if report.when == "call":
        if report.failed and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path(working_root, "test-reports/screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            screen_file = str(f"{uuid.uuid1()}.png")
            img_path = os.path.join(screenshot_dir, screen_file)
            page.screenshot(path=img_path)
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # add the screenshots to the html report
            extra.append(pytest_html.extras.png(img_path))
        report.extra = extra


@pytest.fixture
def page(page: Page) -> Page:
    timeout = 10000
    page.set_default_navigation_timeout(timeout)
    page.set_default_timeout(timeout)
    return page


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev")


@pytest.fixture(scope='session', autouse=True)
def env_name(request):
    return request.config.getoption("--env")


@pytest.fixture(scope='session')
def base_url(env_name):
    if env_name == 'dev':
        return 'https://www.saucedemo.com'
    if env_name == 'prod':
        return 'https://www.saucedemo.com'
    sys.exit('Please provide a valid environment')


@pytest.fixture(scope='function')
def authoriz_page(page, base_url):
    login_page = Login(page)
    login_page.goto(base_url)
    login_page.login(User.USERNAME, User.PASSWORD)
    return page


@pytest.fixture(scope='function')
def product_page(authoriz_page):
    return Products(authoriz_page)


@pytest.fixture(scope='function')
def cart_page(authoriz_page):
    return Cart(authoriz_page)


@pytest.fixture(scope='function')
def checkout_pages(authoriz_page):
    checkout_one_page = CheckoutOne(authoriz_page)
    checkout_two_page = CheckoutTwo(authoriz_page)
    complete_page = Complete(authoriz_page)
    return checkout_one_page, checkout_two_page, complete_page

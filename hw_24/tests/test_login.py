import pytest
from playwright.sync_api import Page, expect
from pages.login_page import Login
from test_data.users import User


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_successful_login(page: Page, base_url, logger):
    logger.info("Testing successful user authorization")

    login_page = Login(page)
    login_page.goto(base_url)

    login_page.login(User.USERNAME, User.PASSWORD)
    logger.info("Verifying successful login")

    expect(page).to_have_url(f"{base_url}/inventory.html")
    logger.info("User authorization test passed")

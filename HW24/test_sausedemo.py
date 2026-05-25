"""
Tests for logging in, adding items to cart, and checking out: https://www.saucedemo.com/
"""


import pytest
from playwright.sync_api import sync_playwright, expect
from logging_config import get_logger

logger = get_logger(__name__)


@pytest.fixture
def page():
    logger.info("Setting up test environment")
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()
    logger.info("Tearing down test environment")


@pytest.fixture
def authoriz_page(page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    with page.expect_navigation():
        page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    logger.info("Authorization was successful")
    yield page


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.login
def test_login(page):
    logger.info("Testing successful user authorization")

    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    logger.debug("The login and password fields are filled in")

    with page.expect_navigation():
        page.locator("[data-test=\"login-button\"]").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")

    logger.info("User authorization test passed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_add_to_cart(authoriz_page):
    logger.info("Testing adding a product to the cart")

    authoriz_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(authoriz_page.locator("[data-test=\"shopping-cart-badge\"]")).to_have_text("1")
    with authoriz_page.expect_navigation():
        authoriz_page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(authoriz_page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(authoriz_page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    expect(authoriz_page.locator("[data-test=\"cart-list\"]")).to_be_visible()
    expect(authoriz_page.locator("[data-test=\"item-4-title-link\"]")).to_be_visible()

    logger.info("Adding product to cart test passed")

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_add_to_cart_2(authoriz_page):
    logger.info("Testing adding multiple items to cart")

    authoriz_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    authoriz_page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    expect(authoriz_page.locator("[data-test=\"shopping-cart-badge\"]")).to_have_text("2")
    with authoriz_page.expect_navigation():
        authoriz_page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(authoriz_page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(authoriz_page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    expect(authoriz_page.locator("[data-test=\"cart-list\"]")).to_be_visible()
    expect(authoriz_page.locator("[data-test=\"item-4-title-link\"]")).to_be_visible()
    expect(authoriz_page.locator("[data-test=\"item-0-title-link\"]")).to_be_visible()

    logger.info("Adding multiple items to cart test passed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.checkout
def test_cart_checkout(authoriz_page):
    logger.info("Testing cart checkout")

    authoriz_page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    expect(authoriz_page.locator("[data-test=\"shopping-cart-badge\"]")).to_have_text("1")
    with authoriz_page.expect_navigation():
        authoriz_page.locator("[data-test=\"shopping-cart-link\"]").click()
    expect(authoriz_page).to_have_url("https://www.saucedemo.com/cart.html")

    with authoriz_page.expect_navigation():
        authoriz_page.locator("[data-test=\"checkout\"]").click()
    expect(authoriz_page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    expect(authoriz_page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    authoriz_page.locator("[data-test=\"firstName\"]").fill("test_name")
    authoriz_page.locator("[data-test=\"lastName\"]").fill("test_lastname")
    authoriz_page.locator("[data-test=\"postalCode\"]").fill("000000")
    logger.debug("The fields in the 'Checkout: Your Information' section are filled in.")

    with authoriz_page.expect_navigation():
        authoriz_page.locator("[data-test=\"continue\"]").click()
    expect(authoriz_page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(authoriz_page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Overview")
    expect(authoriz_page.locator("[data-test=\"payment-info-label\"]")).to_contain_text("Payment Information:")
    expect(authoriz_page.locator("[data-test=\"shipping-info-label\"]")).to_contain_text("Shipping Information:")
    expect(authoriz_page.locator("[data-test=\"total-info-label\"]")).to_contain_text("Price Total")

    with authoriz_page.expect_navigation():
        authoriz_page.locator("[data-test=\"finish\"]").click()
    expect(authoriz_page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(authoriz_page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Complete!")
    expect(authoriz_page.locator("[data-test=\"checkout-complete-container\"]")).to_be_visible()

    with authoriz_page.expect_navigation():
        authoriz_page.locator("[data-test=\"back-to-products\"]").click()
    expect(authoriz_page).to_have_url("https://www.saucedemo.com/inventory.html")

    logger.info("Checkout in the shopping cart test passed")

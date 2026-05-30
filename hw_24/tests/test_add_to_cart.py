import pytest
from playwright.sync_api import expect
from ..test_data.prod_data import ProdData


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_add_item_to_cart(product_page, cart_page, logger):
    logger.info("Testing adding a product to the cart")

    product_page.add_to_cart("Sauce Labs Backpack")
    logger.info("Product added to the cart")
    expect(product_page.cart_badge()).to_have_text("1")

    product_page.open_shopping_cart()
    logger.info("Redirected to the shopping cart page")

    expect(product_page.page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart_page.title).to_have_text("Your Cart")
    expect(cart_page.cart_list()).to_be_visible()
    expect(cart_page.cart_item_by_id(ProdData.BACKPACK_ID)).to_be_visible()

    logger.info("Adding product to cart test passed")


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.cart
def test_add_item_to_cart2(product_page, cart_page, logger):
    logger.info("Testing adding multiple items to cart")

    product_page.add_to_cart("Sauce Labs Backpack")
    logger.info("First product (Sauce Labs Backpack) added to the cart")

    product_page.add_to_cart("Sauce Labs Bike Light")
    logger.info("Second product (Sauce Labs Bike Light) added to the cart")

    expect(product_page.cart_badge()).to_have_text("2")
    logger.info("Cart badge shows 2 items")

    product_page.open_shopping_cart()
    logger.info("Redirected to the shopping cart page")

    expect(product_page.page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cart_page.title).to_have_text("Your Cart")
    expect(cart_page.cart_list()).to_be_visible()
    expect(cart_page.cart_item_by_id(ProdData.BACKPACK_ID)).to_be_visible()
    expect(cart_page.cart_item_by_id(ProdData.BIKE_ID)).to_be_visible()

    logger.info("Adding multiple items to cart test passed")

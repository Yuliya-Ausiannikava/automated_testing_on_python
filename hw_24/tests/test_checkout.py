import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.checkout
def test_cart_checkout(product_page, cart_page, checkout_pages, logger):
    logger.info("Testing cart checkout")

    product_page.add_to_cart("backpack")
    logger.info("Product added to the cart")

    product_page.open_shopping_cart()
    logger.info("Redirected to the shopping cart page")

    cart_page.checkout()
    logger.info("Redirecting to the first step of payment: Your Information")
    expect(cart_page.page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    checkout_one_page, checkout_two_page, complete_page = checkout_pages

    expect(checkout_one_page.checkout_one_title()).to_contain_text("Checkout: Your Information")

    checkout_one_page.fill_checkout_info()
    logger.debug("The fields in the 'Checkout: Your Information' section are filled in.")

    checkout_one_page.click_continue()
    logger.info("Redirecting to the second step of payment: Overview")
    expect(checkout_one_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(checkout_two_page.checkout_two_title()).to_contain_text("Checkout: Overview")
    expect(checkout_two_page.payment_info()).to_contain_text("Payment Information")
    expect(checkout_two_page.shipping_info()).to_contain_text("Shipping Information")
    expect(checkout_two_page.price_total()).to_contain_text("Price Total")

    checkout_two_page.finish()
    logger.info("Redirect to the order confirmation page")
    expect(checkout_two_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(complete_page.complete_title()).to_contain_text("Checkout: Complete!")

    complete_page.back_home()
    logger.info("Redirect to home page")
    expect(complete_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    logger.info("Checkout in the shopping cart test passed")

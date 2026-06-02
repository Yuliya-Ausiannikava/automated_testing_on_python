from playwright.sync_api import Page
from .base_page import BasePage
from .navbar_page import Navbar


class CheckoutTwo(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(page)

    # Locators
    def checkout_two_title(self):
        return self.page.locator('[data-test="title"]')

    def cart_list(self):
        return self.page.locator('[data-test="cart-list"]')

    def payment_info(self):
        return self.page.locator('[data-test="payment-info-label"]')

    def shipping_info(self):
        return self.page.locator('[data-test="shipping-info-label"]')

    def price_total(self):
        return self.page.locator('[data-test="total-info-label"]')

    def cancel_button(self):
        return self.page.locator('[data-test="cancel"]')

    def finish_button(self):
        return self.page.locator('[data-test="finish"]')

    # Actions on the Checkout page (step two)
    def finish(self):
        with self.page.expect_navigation():
            self.finish_button().click()

    def cancel(self):
        with self.page.expect_navigation():
            self.cancel_button().click()

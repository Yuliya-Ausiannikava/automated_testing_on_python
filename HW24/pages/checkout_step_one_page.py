from playwright.sync_api import Page
from base_page import BasePage
from navbar_page import Navbar
from ..test_data.checkout_data import CheckoutInfo


class CheckoutOne(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(page)

    # Locators
    def checkout_one_title(self):
        return self.page.locator('[data-test="title"]')

    def first_name(self):
        return self.page.locator('[data-test="firstName"]')

    def last_name(self):
        return self.page.locator('[data-test="lastName"]')

    def postal_code(self):
        return self.page.locator('[data-test="postalCode"]')

    def cancel_button(self):
        return self.page.locator('[data-test="cancel"]')

    def continue_button(self):
        return self.page.locator('[data-test="continue"]')

    # Actions on the Checkout page (step one)
    def fill_checkout_info(self):
        self.first_name_input().fill(CheckoutInfo.FIRSTNAME)
        self.last_name_input().fill(CheckoutInfo.LASTNAME)
        self.postal_code_input().fill(CheckoutInfo.POSTCODE)

    def click_continue(self):
        with self.page.expect_navigation():
            self.continue_button().click()

    def click_cancel(self):
        with self.page.expect_navigation():
            self.cancel_button().click()

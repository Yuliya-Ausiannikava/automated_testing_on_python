from playwright.sync_api import Page
from .base_page import BasePage
from .navbar_page import Navbar


class Cart(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(page)

    # Shopping cart locators
    def title(self):
        return self.page.locator('[data-test="title"]')

    def cart_list(self):
        return self.page.locator('[data-test="cart-list"]')

    def cart_item_by_id(self, item_numb: str):
        return self.page.locator(f"[data-test='{item_numb}']")

    def checkout_button(self):
        return self.page.locator('[data-test="checkout"]')

    def continue_shopping_button(self):
        return self.page.locator('[data-test="continue-shopping"]')

    # Actions in the shopping cart
    def checkout(self):
        with self.page.expect_navigation():
            self.checkout_button().click()

    def remove(self, item_id: str):
        self.page.locator(f'[data-test="remove-sauce_labs-{item_id}"]').click()

    def continue_shopping(self):
        with self.page.expect_navigation():
            self.continue_shopping_button().click()

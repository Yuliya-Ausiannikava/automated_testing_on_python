from playwright.sync_api import Page
from base_page import BasePage
from navbar_page import Navbar


class Cart(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(page)

    # Shopping cart locators
    def title(self):
        return self.page.locator('[data-test="title"]')

    def cart_list(self):
        return self.page.locator('[data-test="cart-list"]')

    def cart_item_by_id(self, item_id: str):
        return self.page.locator(f"[data-test='{item_id}']")

    def checkout_button(self):
        return self.page.locator('[data-test="checkout"]')

    def continue_shopping_button(self):
        return self.page.locator('[data-test="continue-shopping"]')

    # Actions in the shopping cart
    def checkout(self):
        with self.page.expect_navigation():
            self.checkout_button().click()

    def remove_item(self, item_name: str):
        self.cart_item(item_name).get_by_text('Remove').click()

    def continue_shopping(self):
        with self.page.expect_navigation():
            self.continue_shopping_button().click()

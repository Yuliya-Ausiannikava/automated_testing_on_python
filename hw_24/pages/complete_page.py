from playwright.sync_api import Page
from .base_page import BasePage
from .navbar_page import Navbar


class Complete(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(page)

    # Locators
    def complete_title(self):
        return self.page.locator('[data-test="title"]')

    def back_home_button(self):
        return self.page.locator('[data-test="back-to-products"]')

    # Actions for the completion page
    def back_home(self):
        with self.page.expect_navigation():
            self.back_home_button().click()

from playwright.sync_api import Page
from base_page import BasePage


class Navbar(BasePage):
    def __init__(self, page: Page):
        self.page = page
        super().__init__(page)

    def logo(self):
        return self.page.locator('[class="app_logo"]')

    def burger_menu(self):
        return self.page.locator('#react-burger-menu-btn')

    def cart(self):
        return self.page.locator('[class="shopping_cart_link"]')
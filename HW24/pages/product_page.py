from playwright.sync_api import Page
from base_page import BasePage
from navbar_page import Navbar

class Products(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.navbar = Navbar(page)


    # Locators
    def products_title(self):
        return self.page.locator('[data-test="title"]')

    def product_list(self):
        return self.page.locator('[data-test="inventory_list"]')

    def product_sort(self):
        return self.page.locator('[data-test="product_sort_container"]')

    def cart_badge(self):
        return self.page.locator('[data-test="shopping-cart-badge"]')


    # Actions on the product page
    def get_products_title_text(self):
        return self.products_title().inner_text()

    def add_to_cart(self, product_name: str):
        self.page.locator(f'[data-test="add-to-cart-sauce-labs-{product_name}"]').click()

    def remove(self, product_name: str):
        self.page.locator(f'[data-test="remove-{product_name}"]').click()

    def open_shopping_cart(self):
        with self.page.expect_navigation():
            self.page.locator('[data-test="shopping-cart-link"]').click()

    def open_burger_menu(self):
        self.page.locator('#react-burger-menu-btn').click()

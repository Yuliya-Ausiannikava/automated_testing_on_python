from playwright.sync_api import Page
from base_page import BasePage


class Login(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.login_input = page.get_by_placeholder('USERNAME')
        self.password_input = page.get_by_placeholder('PASSWORD')
        self.login_button = page.get_by_role('button', name='Login')
        super().__init__(page)

    def login(self, username: str, password: str):
        self.login_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

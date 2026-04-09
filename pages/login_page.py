from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://passport.rusneb.ru/auth/realms/RSL/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Fwww.rsl.ru%2Flogin&client_id=rsl.ru&scope=rsl_udb_profile+openid")
        self._username_input = self.page.locator("input[name='username']")
        self._password_input = page.locator("input[name='password']")
        self._login_button = page.locator("button[name='login']")
        self._error_message = page.locator(".alert.alert-error .kc-feedback-text")

    def get_username_input(self):
        return self._username_input

    def get_password_input(self):
        return self._password_input

    def get_login_button(self):
        return self._login_button

    def fill_username_input(self, username: str):
        self._username_input.fill(username)

    def fill_password_input(self, password: str):
        self._password_input.fill(password)

    def click_login_button(self):
        self._login_button.click()

    def get_error_message(self):
        return self._error_message
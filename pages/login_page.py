from playwright.sync_api import Page
from pages.base_page import BasePage
from controls.input import Input
from controls.button import Button
from controls.link import Link
from controls.error_message import ErrorMessage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://passport.rusneb.ru/auth/realms/RSL/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Fwww.rsl.ru%2Flogin&client_id=rsl.ru&scope=rsl_udb_profile+openid")
        self.username_input = Input(page, page.locator("input[name='username']"))
        self.password_input = Input(page, page.locator("input[name='password']"))
        self.login_button = Button(page, page.locator("button[name='login']"))
        self.error_message = ErrorMessage(page, page.locator(".alert.alert-error .kc-feedback-text"))
        self.forgot_password_link = Link(page, page.locator("a.sign-in__forgot-password"))
        self.reset_email_input = Input(page, page.locator("input#email, input[name='username'].sign-in__form-input"))
        self.reset_submit_button = Button(page, page.locator("button.sign-in__entry-button[type='submit']"))
        self.reset_instruction_text = Input(page, page.locator(".first-step-registration__notification-text"))
        self.success_message = ErrorMessage(page, page.locator(".kc-feedback-text"))
        self.email_error = ErrorMessage(page, page.locator(".email_exception"))

    def get_username_input(self) -> Input:
        return self.username_input

    def get_password_input(self) -> Input:
        return self.password_input

    def get_login_button(self) -> Button:
        return self.login_button

    def get_error_message(self) -> ErrorMessage:
        return self.error_message

    def get_forgot_password_link(self) -> Link:
        return self.forgot_password_link

    def get_reset_email_input(self) -> Input:
        return self.reset_email_input

    def get_reset_submit_button(self) -> Button:
        return self.reset_submit_button

    def get_reset_instruction_text(self) -> Input:
        return self.reset_instruction_text

    def get_success_message(self) -> ErrorMessage:
        return self.success_message

    def get_email_error(self) -> ErrorMessage:
        return self.email_error

    def fill_username_input(self, username: str):
        self.username_input.fill(username)

    def fill_password_input(self, password: str):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def click_forgot_password_link(self):
        self.forgot_password_link.click()

    def fill_reset_email_input(self, email: str):
        self.reset_email_input.fill(email)

    def click_reset_submit_button(self):
        self.reset_submit_button.click()
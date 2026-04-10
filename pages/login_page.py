from playwright.sync_api import Page
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, url = "https://passport.rusneb.ru/auth/realms/RSL/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Fwww.rsl.ru%2Flogin&client_id=rsl.ru&scope=rsl_udb_profile+openid")
        self._username_input = self.page.locator("input[name='username']")
        self._password_input = page.locator("input[name='password']")
        self._login_button = page.locator("button[name='login']")
        self._error_message = page.locator(".alert.alert-error .kc-feedback-text")
        self._forgot_password_link = page.locator("a.sign-in__forgot-password")
        self._reset_email_input = page.locator("input#email, input[name='username'].sign-in__form-input")
        self._reset_submit_button = page.locator("button.sign-in__entry-button[type='submit']")
        self._reset_instruction_text = page.locator(".first-step-registration__notification-text")
        self._success_message = page.locator(".kc-feedback-text")
        self._email_error = page.locator(".email_exception")

    def get_username_input(self):
        """Метод возвращает поле ввода Email"""
        return self._username_input

    def get_password_input(self):
        """Метод возвращает поле ввода пароля"""
        return self._password_input

    def get_login_button(self):
        """Метод возвращает кнопку Войти"""
        return self._login_button

    def fill_username_input(self, username: str):
        self._username_input.fill(username)

    def fill_password_input(self, password: str):
        self._password_input.fill(password)

    def click_login_button(self):
        self._login_button.click()

    def get_error_message(self):
        return self._error_message

    def get_forgot_password_link(self):
        """Метод возвращает локатор ссылки Забыли пароль"""
        return self._forgot_password_link

    def click_forgot_password_link(self):
        """Метод кликает по кнопке Забыли пароль"""
        self._forgot_password_link.click()

    def get_reset_instruction_text(self):
        """Возвращает локатор текста-инструкции на странице восстановления пароля"""
        return self._reset_instruction_text

    def get_reset_email_input(self):
        """Метод возвращает поле ввода Email для фвосстановления"""
        return self._reset_email_input

    def get_reset_submit_button(self):
        """Метод возвращает кнопку Поулчить пароль"""
        return self._reset_submit_button

    def fill_reset_email_input(self, email: str):
        self._reset_email_input.fill(email)

    def click_reset_submit_button(self):
        """Метод кликает на кнопку Получить пароль"""
        self._reset_submit_button.click()

    def get_success_message(self):
        """Возвращает локатор сообщения об успешной отправке запроса"""
        return self._success_message

    def get_email_error(self):
        """Метод  возвращает локатор сообщения об ошибке валидации email"""
        return self._email_error
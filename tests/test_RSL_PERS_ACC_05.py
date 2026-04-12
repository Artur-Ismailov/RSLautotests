import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.title("Запрос на восстановление пароля с невалидным email")
def test_RSL_PERS_ACC_05(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()

    with allure.step("1. В шапке сайта кликнуть на кнопку [Личный кабинет]"):
        home_page.click_button_resonal_account()

        assert "https://passport.rusneb.ru/auth/realms/RSL/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Fwww.rsl.ru%2Flogin&client_id=rsl.ru&scope=rsl_udb_profile+openid" in login_page.url

        expect(login_page.get_username_input().locator).to_be_visible()
        expect(login_page.get_password_input().locator).to_be_visible()
        expect(login_page.get_login_button().locator).to_be_visible()
        expect(login_page.get_forgot_password_link().locator).to_be_visible()

    with allure.step("2. Кликнуть на ссылку «Забыли пароль?»"):
        login_page.click_forgot_password_link()

        expect(login_page.get_reset_instruction_text().locator).to_be_visible(timeout=5000)
        expect(login_page.get_reset_instruction_text().locator).to_contain_text(
            "Введите ваш адрес электронной почты и мы вышлем вам инструкцию по получению нового пароля", timeout=5000)
        expect(login_page.get_reset_email_input().locator).to_be_visible(timeout=5000)
        expect(login_page.get_reset_submit_button().locator).to_be_visible()

    with allure.step("3. В поле ввода «Адрес электронной почты» ввести «test@invalid»"):
        login_page.fill_reset_email_input("test@invalid")

        expect(login_page.get_reset_email_input().locator).to_have_value("test@invalid", timeout=5000)

    with allure.step("4. Кликнуть на кнопку [Получить пароль]"):
        login_page.click_reset_submit_button()

        expect(login_page.get_email_error().locator).to_be_visible(timeout=5000)
        expect(login_page.get_email_error().locator).to_have_text("Ошибка! Неверный формат", timeout=5000)
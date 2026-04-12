import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.title("Авторизация с невалидными учетными данными")
def test_RSL_PERS_ACC_01(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()

    with allure.step("1. В шапке сайта кликнуть на кнопку [Личный кабинет]"):
        home_page.click_button_resonal_account()

        assert "https://passport.rusneb.ru/auth/realms/RSL/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Fwww.rsl.ru%2Flogin&client_id=rsl.ru&scope=rsl_udb_profile+openid" in login_page.url

        expect(login_page.get_username_input().locator).to_be_visible()
        expect(login_page.get_password_input().locator).to_be_visible()
        expect(login_page.get_login_button().locator).to_be_visible()

    with allure.step("2. В поле ввода «Адрес электронной почты или номер читательского билета» ввести «invalid@mail.ru»"):
        login_page.fill_username_input("invalid@mail.ru")

        expect(login_page.get_username_input().locator).to_have_value("invalid@mail.ru", timeout=5000)

    with allure.step("3. В поле ввода «Пароль» ввести «password»"):
        login_page.fill_password_input("password")

        expect(login_page.get_password_input().locator).to_have_value("password", timeout=5000)

    with allure.step("4. Кликнуть на кнопку [Войти]"):
        login_page.click_login_button()

        expect(login_page.get_error_message().locator).to_be_visible(timeout=10000)
        expect(login_page.get_error_message().locator).to_contain_text("Неправильное имя пользователя или пароль", timeout=5000)
        expect(login_page.get_error_message().locator).to_contain_text("Или данные были удалены согласно 152-ФЗ", timeout=5000)
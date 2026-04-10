import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.title("Авторизация с валидными учетными данными")
def test_RSL_PERS_ACC_02(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()

    with allure.step("1. В шапке сайта кликнуть на кнопку [Личный кабинет]"):
        home_page.click_button_resonal_account()

        assert "https://passport.rusneb.ru/auth/realms/RSL/protocol/openid-connect/auth?response_type=code&redirect_uri=https%3A%2F%2Fwww.rsl.ru%2Flogin&client_id=rsl.ru&scope=rsl_udb_profile+openid" in login_page.url

        expect(login_page.get_username_input()).to_be_visible()
        expect(login_page.get_password_input()).to_be_visible()
        expect(login_page.get_login_button()).to_be_visible()

    with allure.step("2. В поле ввода «Адрес электронной почты или номер читательского билета» ввести «qatester12348765@mail.ru»"):
        login_page.fill_username_input("qatester12348765@mail.ru")

        expect(login_page.get_username_input()).to_have_value("qatester12348765@mail.ru", timeout=5000)

    with allure.step("3. В поле ввода «Пароль» ввести «QAtester1234»"):
        login_page.fill_password_input("QAtester1234")

        expect(login_page.get_password_input()).to_have_value("QAtester1234", timeout=5000)

    with allure.step("4. Кликнуть на кнопку [Войти]"):
        login_page.click_login_button()

        assert "https://www.rsl.ru/" in home_page.url, "URL != 'https://www.rsl.ru/'"

        expect(home_page.get_usermane_in_button_profile_menu()).to_be_visible(timeout=5000)
        expect(home_page.get_usermane_in_button_profile_menu()).to_have_text("NameTest", timeout=5000)
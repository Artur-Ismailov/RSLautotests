import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.login_page import LoginPage


@allure.title("Успешный выход из системы")
def test_RSL_PERS_ACC_03(page: Page):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    home_page.open()
    home_page.click_button_resonal_account()
    login_page.fill_username_input("qatester12348765@mail.ru")
    login_page.fill_password_input("QAtester1234")
    login_page.click_login_button()

    with allure.step("1. В шапке сайта навести курсор на кнопку [NameTest](имя пользователя)"):
        home_page.hover_over_button_profile_menu()

        expect(home_page.get_dropdown_profile_menu()).to_be_visible(timeout=5000)
        expect(home_page.get_profile_link_in_dropdown()).to_be_visible(timeout=5000)
        expect(home_page.get_profile_link_in_dropdown()).to_have_text("Профиль", timeout=5000)
        expect(home_page.get_logout_link_in_dropdown()).to_be_visible(timeout=5000)
        expect(home_page.get_logout_link_in_dropdown()).to_have_text("Выйти", timeout=5000)

    with allure.step("2. В выпадающем меню кликнуть на кнопку [Выйти]"):
        home_page.click_logout_in_dropdown()

        expect(home_page._header.get_button_resonal_account()).to_be_visible(timeout=10000)
        expect(home_page._header.get_button_resonal_account()).to_have_text("Личный кабинет", timeout=5000)
import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage


@allure.title("Открытие выпадающего меню при наведении")
def test_RSL_NAV_01(page: Page):
    home_page = HomePage(page)
    home_page.open()

    with (allure.step("1.Навести курсор на пункт меню «Читателям»")):
        home_page.hover_over_button_in_menu("Читателям")

        expect(home_page.get_dpordown_menu_readers()).to_be_visible(timeout=5000), "Выпадающе меню не отображается"

    with allure.step("2.Убрать курсор с пункта меню «Читателям»"):
        home_page.hover_over_button_in_menu("Профессионалам")

        expect(home_page.get_dpordown_menu_readers()).not_to_be_visible(timeout=5000), "Выпадающее меню отображается"
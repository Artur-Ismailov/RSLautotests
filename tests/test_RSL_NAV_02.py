import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.readers_page import ReadersPage


@allure.title("Переход по пункту главного меню")
def test_RSL_NAV_02(page: Page):
    home_page = HomePage(page)
    readers_page = ReadersPage(page)
    home_page.open()

    with (allure.step("1.Навести курсор на пункт меню «Читателям»")):
        home_page.hover_over_button_in_menu("Читателям")

        expect(home_page.get_dpordown_menu_readers()).to_be_visible(timeout=5000)

    with allure.step("2.Кликнуть на пункт меню «Читателям»"):
        home_page.click_button_menu_by_title("Читателям")

        assert "https://www.rsl.ru/ru/4readers/" in readers_page.url

        expect(readers_page.get_page_title_h1()).to_have_text("Читателям", timeout=5000)

        expect(readers_page.get_reader_subsection_elements()).to_have_count(14, timeout=5000)

import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.search_page import SearchPage


@allure.title("Поиск с набором специальных символов")
def test_RSL_SRCH_04(page: Page):
    home_page = HomePage(page)
    home_page.open()
    special_characters = "@#$%^&*"

    with allure.step("1. Ввести в поле ввода «Поиск по электронному каталогу» последовательность специальных символов «@#$%^&*»"):
        home_page.fill_search_field(special_characters)

        assert home_page._header.get_search_catalog().get_value() == special_characters

    with allure.step("2. Нажать кнопку поиска"):
        search_button_locator = home_page._header._search_button.locator

        new_page = home_page.wait_for_new_tab_from_locator(search_button_locator)

        home_page.wait_for_page_load(new_page)

        assert "https://search.rsl.ru/ru/search" in new_page.url

        search_page = SearchPage(new_page)

        search_page._search_content.wait_for_search_results()

        #assert search_page._search_content.contains_document_text(special_characters)
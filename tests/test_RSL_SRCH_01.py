import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.search_page import SearchPage


@allure.title("Поиск по названию книги")
def test_RSL_SRCH_01(page: Page):
    home_page = HomePage(page)
    home_page.open()
    document_title = "Война и мир"

    with (allure.step("1.Ввести в поле поиска «Поиск по электронному каталогу» текст «Война и мир»")):
        home_page.fill_search_field(document_title)

        expect(home_page.get_search_field_locator()).to_have_value(document_title)

    with allure.step("2. Нажать кнопку поиска"):
        search_button_locator = home_page.get_button_search()
        new_page = home_page.wait_for_new_tab_from_locator(search_button_locator)
        home_page.wait_for_page_load(new_page)

        search_page = SearchPage(new_page)
        search_page.wait_for_search_results()

        assert "https://search.rsl.ru/ru/search" in search_page.url
        assert search_page.contains_document_text(document_title)
import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.search_page import SearchPage


@allure.title("Поиск по  фамилии автора")
def test_RSL_SRCH_02(page: Page):
    home_page = HomePage(page)
    home_page.open()
    author_surname = "Лев Толстой"

    with allure.step("1.Ввести в поле поиска «Поиск по электронному каталогу» текст «Лев Толстой»"):
        home_page.fill_search_field(author_surname)

        assert home_page.get_value_in_input_field() == author_surname

    with allure.step("2. Нажать кнопку поиска"):
        search_button_locator = home_page._header._search_button.locator

        new_page = home_page.wait_for_new_tab_from_locator(search_button_locator)

        home_page.wait_for_page_load(new_page)

        assert "https://search.rsl.ru/ru/search" in new_page.url

        search_page = SearchPage(new_page)

        search_page._search_content.wait_for_search_results()

        assert search_page._search_content.contains_document_text(author_surname)
import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.search_page import SearchPage


@allure.title("Поиск по пустой строке")
def test_RSL_SRCH_03(page: Page):
    home_page = HomePage(page)
    home_page.open()

    with allure.step("1. Нажать кнопку поиска"):
        search_button_locator = home_page.get_button_search()
        new_page = home_page.wait_for_new_tab_from_locator(search_button_locator)
        home_page.wait_for_page_load(new_page)

        search_page = SearchPage(new_page)
        search_page.wait_for_search_results()

        assert "https://search.rsl.ru/" in search_page.url
        assert search_page.search_results()
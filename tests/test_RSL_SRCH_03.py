import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.search_page import SearchPage


@allure.title("Поиск по пустой строке")
def test_RSL_SRCH_03(page: Page):
    home_page = HomePage(page)
    home_page.open()
    filter_text = "По дате поступл-я в ЭК РГБ (по убыв.) "

    with allure.step("1. Нажать кнопку поиска"):
        search_button_locator = home_page._header._search_button.locator
        new_page = home_page.wait_for_new_tab_from_locator(search_button_locator)
        home_page.wait_for_page_load(new_page)

        assert "https://search.rsl.ru/" in new_page.url

        search_page = SearchPage(new_page)
        search_page._search_content.wait_for_search_results()

        assert search_page._active_filters.contains_active_filter_text(filter_text)
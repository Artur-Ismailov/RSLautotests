import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.search_page import SearchPage


@allure.title("Поиск по запросу максимальной допустимой длины")
def test_RSL_SRCH_06(page: Page):
    home_page = HomePage(page)
    home_page.open()
    text = "A" * 256

    with allure.step("1. Ввести в поле поиска рыбный текст состоящий из 256 латинских символов"):
        home_page.fill_search_field(text)

        assert home_page.get_value_in_input_field() == text, "В поиске не отображается введенный текст"

    with allure.step("2. Нажать кнопку поиска"):
        search_button_locator = home_page.get_button_search()
        new_page = home_page.wait_for_new_tab_from_locator(search_button_locator)
        home_page.wait_for_page_load(new_page)

        assert "https://search.rsl.ru/ru/search" in new_page.url

        search_page = SearchPage(new_page)

        assert search_page.no_search_results()
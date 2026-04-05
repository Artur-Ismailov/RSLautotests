import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage


@allure.title("Поиск по названию книги")
def test_RSL_SRCH_01(page: Page):
    home_page = HomePage(page)
    home_page.open()
    document_title = "Война и мир"

    with allure.step("1.Ввести в поле поиска «Поиск по электронному каталогу» текст «Война и мир»"):
        home_page.fill_search_field(document_title)

        assert home_page._header.get_search_catalog().get_value() == document_title

    with allure.step("2. Нажать кнопку поиска"):
        with page.expect_popup() as popup_info:
            home_page.click_search_button()

        new_page = popup_info.value

        # Ждём загрузки страницы
        new_page.wait_for_load_state()

        new_page.wait_for_url("*https://search.rsl.ru/ru/search*", timeout=30000)
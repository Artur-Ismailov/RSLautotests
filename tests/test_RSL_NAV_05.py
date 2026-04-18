import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.readers_page import ReadersPage
from pages.work_schedule_page import WorkSchedulePage
from pages.how_join_page import HowJoinPage


@allure.title("Проверка доступности ссылок в разделе «Читателям»")
def test_RSL_NAV_05(page: Page):
    home_page = HomePage(page)
    readers_page = ReadersPage(page)
    work_schedule_page = WorkSchedulePage(page)
    how_join_page = HowJoinPage(page)
    home_page.open()

    with allure.step("1.Навести курсор на пункт меню «Читателям»"):
        home_page.hover_over_button_in_menu("Читателям")

        expect(home_page.get_dpordown_menu_readers()).to_be_visible(timeout=5000)

    with allure.step("2.Кликнуть на пункт меню «Читателям»"):
        home_page.click_button_menu_by_title("Читателям")

        assert "https://www.rsl.ru/ru/4readers/" in readers_page.url

        expect(readers_page.get_page_title_h1()).to_have_text("Читателям", timeout=5000)

        expect(readers_page.get_reader_subsection_elements()).to_have_count(14, timeout=5000)

    with allure.step("3. Кликнуть на подраздел «График работы»"):
        readers_page.click_reader_subsection_by_title("График работы")

        assert "https://www.rsl.ru/ru/4readers/schedules/" in work_schedule_page.url

        expect(work_schedule_page.get_page_title_h1()).to_have_text("График работы", timeout=5000)

    with allure.step("4. В хлебных крошках кликнуть «Читателям»"):
        work_schedule_page.click_breadcrumb_by_title("Читателям")

        assert "https://www.rsl.ru/ru/4readers/" in readers_page.url

        expect(readers_page.get_page_title_h1()).to_have_text("Читателям", timeout=5000)

    with allure.step("5. Кликнуть на подраздел «Как записаться»"):
        readers_page.click_reader_subsection_by_title("Как записаться")

        assert "https://www.rsl.ru/ru/4readers/how-to-join" in how_join_page.url

        expect(how_join_page.get_page_title_h1()).to_have_text("Как записаться", timeout=5000)
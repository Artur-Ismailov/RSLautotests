import allure
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.work_schedule_page import WorkSchedulePage
from pages.readers_page import ReadersPage


@allure.title("Переход на страницу 'Читателям' по хлебным крошкам")
def test_RSL_NAV_04(page: Page):
    home_page = HomePage(page)
    work_schedule_page = WorkSchedulePage(page)
    readers_page = ReadersPage(page)
    home_page.open()

    with (allure.step("1.Навести курсор на пункт меню «Читателям»")):
        home_page.hover_over_button_in_menu("Читателям")

        expect(home_page.get_dpordown_menu_readers()).to_be_visible(timeout=5000), "Выпадающе меню не отображается"

    with allure.step("2.В выпадающем списке кликнуть «График работы»"):
        home_page.click_button_menu_by_title("График работы")

        assert "https://www.rsl.ru/ru/4readers/schedules/" in work_schedule_page.url

        expect(work_schedule_page.get_page_title_h1()).to_have_text("График работы", timeout=5000), "Заголовок !='График работы'"

        expect(work_schedule_page.get_breadcrumbs_container()).to_be_visible(timeout=5000), "Хлебные крошки не отображаются"
        expect(work_schedule_page.get_breadcrumb_home_link()).to_be_visible(), "'Главная' не отображается в хлебных крошках"
        expect(work_schedule_page.get_breadcrumb_readers_link()).to_be_visible(), "'Читателям' не отображается в хлебных крошках"

    with allure.step("3. В хлебных крошках кликнуть «Читателям»"):
        work_schedule_page.click_breadcrumb_by_title("Читателям")

        assert "https://www.rsl.ru/ru/4readers/" in readers_page.url

        expect(readers_page.get_page_title_h1()).to_have_text("Читателям", timeout=5000), "Заголовок страницы !='Читателям'"

        expect(readers_page.get_breadcrumb_home_link()).to_be_visible(), "'Главная' не отображается в хлебных крошках"
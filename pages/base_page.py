from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page, url: str):
        self.page = page
        self.url = url

    def open(self):
        return self.page.goto(self.url)

    def wait_for_url_contains(self, expected_part: str, timeout: int = 30000):
        self.page.wait_for_url(f"*{expected_part}*", timeout=timeout)
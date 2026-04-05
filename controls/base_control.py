from playwright.sync_api import Page, Locator


class BaseControl:
    def __init__(self, page: Page, locator: Locator):
        self.page = page
        self.locator = locator
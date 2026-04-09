from playwright.sync_api import Page, Locator
from controls.base_control import BaseControl


class PersonalAccountButton(BaseControl):
    def __init__(self, page: Page, locator: Locator):
        super().__init__(page, locator)
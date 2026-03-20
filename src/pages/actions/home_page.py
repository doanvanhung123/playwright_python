

import allure
from playwright.sync_api import expect
from src.common.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.login_button = page.locator("//a[@href='/login']")

    @allure.step("Click login button")
    def click_login_button(self):
        self.login_button.click()
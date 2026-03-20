

import allure
from playwright.sync_api import expect
from src.common.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # ===== LOCATORS (XPath) =====
        self.loginButton = page.locator("//li//a[@href='/login']")

    # ===== ACTIONS =====
    @allure.step("Mở trang chủ")
    def click_login_button(self):
        self.click(self.loginButton)

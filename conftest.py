import pytest
from playwright.sync_api import sync_playwright
from src.pages.actions.home_page import HomePage
from src.utils.env_loader import Env


@pytest.fixture(scope="function")
def page():

    with sync_playwright() as p:

        browser_type = getattr(p, Env.BROWSER)

        browser = browser_type.launch(headless=False)

        context = browser.new_context()

        page = context.new_page()
        page.set_default_timeout(30000)
        page.set_default_navigation_timeout(60000)
        page.goto(Env.BASE_URL)

        yield page

        browser.close()

@pytest.fixture
def home_page(page):
    return HomePage(page)
        
# @pytest.fixture
# def login_page(page):
#     return LoginPage(page)
import allure
import pytest

@allure.feature("Tài sản đảm bảo")
@allure.story('Quản lý danh mục DLT Tài sản')
@allure.title("TC022 - 01: Quản lý danh mục đơn vị định giá - Kiểm tra Thêm mới")
@pytest.mark.smoke
def test_open_homepage(home_page):

    home_page.click_login_button()

@allure.feature("Tài sản đảm bảo")
@allure.story('Quản lý danh mục DLT Tài sản')
@allure.title("TC022 - 01: Quản lý danh mục đơn vị định giá - Kiểm tra Thêm mới")
@pytest.mark.regression
def test_open_homepage2(home_page):

    home_page.click_login_button()

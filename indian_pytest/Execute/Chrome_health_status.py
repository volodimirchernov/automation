from selenium.webdriver import Chrome
import pytest

from Base_methods.Export_methods import *
from Base_methods.Mydocs_methods import *
from Base_methods.Home_methods import *


# @pytest.fixture(scope = 'session') - запуск тестов в одной сессии

@pytest.fixture()
def chrome_driver(request):
    driver = Chrome("../Environment/Drivers/chromedriver.exe")
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


def test_one(chrome_driver):
    full_authorize(chrome_driver)
    chooseFilesInMyDocs(chrome_driver)
    choose_export_way(chrome_driver, "save as")
    delete_document_from_list_method(chrome_driver, "1")
    click_view_document_method(chrome_driver, "1")
    click_preview_method(chrome_driver)


@pytest.mark.skip()
def test_second(chrome_driver):
    chrome_driver.get("https://www.pdffiller.com/")
    assert True

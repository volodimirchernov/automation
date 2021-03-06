from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.chrome.options import Options
from Base_methods.Export_methods import *
from Base_methods.Mydocs_methods import *
from Base_methods.Home_methods import *


# @pytest.fixture(scope = 'session') - запуск тестов в одной сессии

@pytest.fixture()
def chrome_driver(request):

    # For maximaze (start)

    options = Options()
    options.add_argument("--start-maximized")
    driver = Chrome("../Environment/Drivers/chromedriver.exe", chrome_options=options)

    # For maximaze (end)

    # Or driver.set_window_size(1200, 800)

    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    #driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


def test_one(chrome_driver):
    full_authorize(chrome_driver)
    fast_enter_to_multi_export(["146573451"], "save")
    click_save_as()

@pytest.mark.skip()
def test_second(chrome_driver):
    chrome_driver.get("https://www.pdffiller.com/")
    assert True

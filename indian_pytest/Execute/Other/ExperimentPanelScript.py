from selenium.webdriver import Chrome
from Base_methods.Common_methods import *
import pytest

project_name_Print_Instruction = "[export] Print instruction"
project_name_Multi_Export = "[export] Multi export"
project_name_Multi_Export_Tooltip = "[export] Multi export tooltip"
project_name_Fillable_Fields_Export = "[Export Worker] Fillable fields export"
project_name_Feedback = "[export] Feedback"

status_test = "0"
status_test2 = "1"

#

login = "iok"
password = "iok"
user_id_test = "11234749"
user_id_test2 = "11257097"

project_name_test = project_name_Fillable_Fields_Export



@pytest.fixture()
def chrome_driver(request):
    driver = Chrome("C:\\Users\\volodimirQA\\Desktop\\drivers\\chromedriver.exe")
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


def add_user_into_experiment(chrome_driver, user_id, project_name, status):
    open_page(chrome_driver, "https://dev5.pdffiller.com/33UMW1ZQ6goFeZ2o/?op=login")

    input_into_field(chrome_driver, ".//input[@type='text']", "iok")
    input_into_field(chrome_driver, ".//input[@type='password']", "iok")
    click_button(chrome_driver, ".//input[@type='submit']")
    click_button(chrome_driver, ".//div[@id='main-menu2']/ul/li[8]")
    input_into_field(chrome_driver, "(.//input[@type='text'])[4]", user_id)
    single_select_from_list_by_text(chrome_driver, ".//select[@id='experiment_id']", project_name)
    single_select_from_list_multi_mode(chrome_driver, ".//select[@id='branch_version']", "index", status)
    click_button(chrome_driver, ".//input[@value='Save']")
    return 0


def test_add_user(chrome_driver):
    add_user_into_experiment(chrome_driver, user_id_test, project_name_test, status_test)

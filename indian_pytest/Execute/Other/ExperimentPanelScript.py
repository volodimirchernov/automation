from selenium.webdriver import Chrome
from selenium import webdriver
from Base_methods.Common_methods import *
import pytest

project_name_Print_Instruction = "[export] Print instruction"
project_name_Multi_Export = "[export] Multi export"
project_name_Multi_Export_Tooltip = "[export] Multi export tooltip"
project_name_Fillable_Fields_Export = "[Export Worker] Fillable fields export"
project_name_Feedback = "[export] Feedback"
project_name_Multi_Print = "[export] Multi export print"
project_name_Menu_Options = "[Header] options menu"

status_off = "0"
status_on = "1"

#

login = "iok"
password = "iok"
user_id_Vova = "11234749"
user_id_Sasha = "11257097"
user_id_Andrey = "11236337"


@pytest.fixture()
def chrome_driver(request):
    driver = Chrome("C:\\Users\\volodimirQA\\Desktop\\drivers\\chromedriver.exe")
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    #driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


def add_user_into_experiment(chrome_driver, arr_user_id, project_name, status):
    open_page(chrome_driver, "https://dev5.pdffiller.com/33UMW1ZQ6goFeZ2o/?op=login")

    input_into_field(chrome_driver, ".//input[@type='text']", "iok")
    input_into_field(chrome_driver, ".//input[@type='password']", "iok")
    click_button(chrome_driver, ".//input[@type='submit']")
    click_button(chrome_driver, ".//div[@id='main-menu2']/ul/li[8]")
    input_into_field(chrome_driver, "(.//input[@type='text'])[4]", id)
    single_select_from_list_by_text(chrome_driver, ".//select[@id='experiment_id']", project_name)
    single_select_from_list_multi_mode(chrome_driver, ".//select[@id='branch_version']", "index", status)
    click_button(chrome_driver, ".//input[@value='Save']")

    return 0


def add_users_into_experiments(chrome_driver, arr_user_id, arr_project_name, status):
    open_page(chrome_driver, "https://dev5.pdffiller.com/33UMW1ZQ6goFeZ2o/?op=login")

    input_into_field(chrome_driver, ".//input[@type='text']", "iok")
    input_into_field(chrome_driver, ".//input[@type='password']", "iok")
    click_button(chrome_driver, ".//input[@type='submit']")
    click_button(chrome_driver, ".//div[@id='main-menu2']/ul/li[8]")

    for id in arr_user_id:
        input_into_field(chrome_driver, "(.//input[@type='text'])[4]", id)
        for project_name in arr_project_name:
            single_select_from_list_by_text(chrome_driver, ".//select[@id='experiment_id']", project_name)
            single_select_from_list_multi_mode(chrome_driver, ".//select[@id='branch_version']", "index", status)
            click_button(chrome_driver, ".//input[@value='Save']")

    return 0


def test_add_users(chrome_driver):
    add_users_into_experiments(chrome_driver, [user_id_Vova, user_id_Andrey, user_id_Sasha], [project_name_Multi_Print, project_name_Menu_Options], status_on)
    #add_user_into_experiment(chrome_driver, user_id_Sasha, project_name_test, status_on)
import time

from Environment.Xpath_library import Xpath_home as h
from Base_methods.Common_methods import *
import Environment.Properties as v

# login_data = "alexbieiqa@testqa.com"
# password_data = "Qawsed123"#
login_data = "volodimirchernov@gmail.com"
password_data = "1"

login_data_test = "chernov.vladimir+paid3@pdffiller.team"
password_data_test = "123321"


# Log In


# Go to home page by url from properties file
def visit_live(driver):
    driver.get(v.live_base_url)
    return True


# Go to log in page by url from properties file
def visit_log_in(driver):
    open_page(driver, v.live_login_url)
    return True


# Go to log in page from home page by button in header
def visit_log_in_page(driver):
    visit_live(driver)
    login_header_Element = driver.find_element_by_xpath(h.xpath_log_in_header_Button)
    click_button(login_header_Element)
    return True


# Input into login filed
def input_login(driver):
    login_field_Element = driver.find_element_by_xpath(h.xpath_login_Field)
    input_into_field(driver, login_field_Element, login_data)
    return True


# Input into password filed
def input_password(driver):
    password_field_Element = driver.find_element_by_xpath(h.xpath_password_Field)
    input_into_field(driver, password_field_Element, password_data)
    return True


# Click on button "Log In"
def press_log_in(driver):
    log_in_submit_Element = driver.find_element_by_xpath(h.xpath_log_in_submit_Button)
    click_button(log_in_submit_Element)
    return True


# Full authorize
def full_authorize(driver):
    visit_live(driver)
    visit_log_in_page(driver)
    input_login(driver)
    input_password(driver)
    press_log_in(driver)
    return True


# Short authorize
def short_authorize(driver):
    visit_log_in(driver)
    input_login(driver)
    input_password(driver)
    press_log_in(driver)
    return True

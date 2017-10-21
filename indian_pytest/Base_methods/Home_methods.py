from Environment.Xpath_library import Xpath_home as h

base_url = "https://www.pdffiller.com/en/"
log_in_url = "https://www.pdffiller.com/en/login.htm/"

login_data = "volodimirchernov@gmail.com"
password_data = "1"


# Log In


# Go to home page by url
def visit_live(driver):
    driver.get(base_url)
    return True


# Go to log in page by url
def visit_log_in(driver):
    driver.get(log_in_url)
    return True


# Go to log in page from home page by button in header
def visit_log_in_page(driver):
    visit_live(driver)
    login_header_Element = driver.find_element_by_xpath(h.xpath_log_in_header_Button)
    login_header_Element.click()
    return True


# Input into login filed
def input_login(driver):
    login_field_Element = driver.find_element_by_xpath(h.xpath_login_Field)
    login_field_Element.clear()
    login_field_Element.send_keys(login_data)
    return True


# Input into password filed
def input_password(driver):
    password_field_Element = driver.find_element_by_xpath(h.xpath_password_Field)
    password_field_Element.clear()
    password_field_Element.send_keys(password_data)
    return True


# Click on button "Log In"
def press_log_in(driver):
    log_in_submit_Element = driver.find_element_by_xpath(h.xpath_log_in_submit_Button)
    log_in_submit_Element.click()
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
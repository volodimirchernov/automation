# help to modify xpath  for clear position
# -- ONLY FOR xpath with construction (xpath)[position]
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.select import Select


def choose_element_position(xpath, necessary_position):
    xpath = xpath.replace("position", necessary_position)
    return xpath


# get url - simple open page
def open_page(chrome_driver, url_text):
    chrome_driver.get(url_text)


# clear field and input text
def input_into_field(chrome_driver, path, text):
    element = chrome_driver.find_element_by_xpath(path)
    element.click()
    element.clear()
    element.send_keys(text)
    return 0


# click on any button
def click_button(chrome_driver, path):
    element = chrome_driver.find_element_by_xpath(path)
    element.click()


# select from list one value by text
def single_select_from_list_by_text(chrome_driver, path, element_text):
    select_list_element = chrome_driver.find_element_by_xpath(path)
    for option in select_list_element.find_elements_by_tag_name('option'):
        if option.text == element_text:
            option.click()
            break


# select from list of values by text
def multi_select_from_list_by_text(chrome_driver, path, elements):
    select_list_element = chrome_driver.chrome_driver.find_element_by_xpath(path)
    for option in select_list_element.find_elements_by_tag_name('option'):
        if option.text in elements:
            option.click()


# Choose from select list by index, or text value
# - multi way by "text", "index"
# - Index begin from 0
def single_select_from_list_multi_mode(chrome_driver, path, way, value):
    select = Select(chrome_driver.find_element_by_xpath(path))
    if way == "index":
        select.select_by_index(value)
    else:
        for option in select.options:
            if option.text == value:
                option.click()
                break


# Get count of web element on page
# - @return int count of elements by xpath
def count_of_elements_by_xpath(chrome_driver, xpath):
    return len(chrome_driver.find_elements_by_xpath(xpath))


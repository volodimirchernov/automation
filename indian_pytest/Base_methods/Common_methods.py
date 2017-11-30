import logging
from webbrowser import Chrome

import Environment.Properties as props
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoAlertPresentException

from selenium.common.exceptions import InvalidSwitchToTargetException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchFrameException

from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotSelectableException

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.support.select import Select


class CommonMethods:
    def find_element_by_xpath(driver, xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            logging.critical("Element was not found")
            return False
        return True

    # help to modify xpath  for clear position
    # -- ONLY FOR xpath with construction (xpath)[position]
    def choose_element_position(path, necessary_position):
        try:
            path = path.replace("position", necessary_position)
        except ValueError:
            logging.error("Incorrect value: text -> " + str(path) + ", text -> " + str(necessary_position))
            return False
        return True

    # get url - simple open page
    def open_page(driver, url_text):
        driver.get(url_text)
        #self.assertTrue("fuck", driver.getCurrentUrl())

    # clear field and input text
    def input_into_field(driver, path, text):
        element = driver.find_element_by_xpath(path)
        element.click()
        element.clear()
        element.send_keys(text)
        return 0

    # click on any button
    def click_button(driver, path):
        element = driver.find_element_by_xpath(path)
        element.click()

    # select from list one value by text
    def single_select_from_list_by_text(driver, path, element_text):
        select_list_element = driver.find_element_by_xpath(path)
        for option in select_list_element.find_elements_by_tag_name('option'):
            if option.text == element_text:
                option.click()
                break

    # select from list of values by text
    def multi_select_from_list_by_text(driver, path, elements):
        select_list_element = driver.chrome_driver.find_element_by_xpath(path)
        for option in select_list_element.find_elements_by_tag_name('option'):
            if option.text in elements:
                option.click()

    # Choose from select list by index, or text value
    # - multi way by "text", "index"
    # - Index begin from 0
    def single_select_from_list_multi_mode(driver, path, way, value):
        select = Select(driver.find_element_by_xpath(path))
        if way == "index":
            select.select_by_index(value)
        else:
            for option in select.options:
                if option.text == value:
                    option.click()
                    break
        return option

    # Fast enter to export page (single)
    # export_way can be "print", "email", "sms", "fax", "save as"
    def fast_enter_to_single_export(project_id, export_way):
        if export_way == "print":
            result_way = props.print_url.replace("[project_id]", project_id)
            return open_page(result_way)
        elif export_way == "email":
            result_way = props.email_url.replace("[project_id]", project_id)
            return open_page(result_way)
        elif export_way == "sms":
            result_way = props.sms_url.replace("[project_id]", project_id)
            return open_page(result_way)
        elif export_way == "fax":
            result_way = props.fax_url.replace("[project_id]", project_id)
            return open_page(result_way)
        elif export_way == "save as":
            result_way = props.email_url.replace("[project_id]", project_id)
            return open_page(result_way)
        else:
            return 0

    # Fast enter to export page (multi)
    # export_way can be "print", "save as"
    def fast_enter_to_multi_export(arr_project_id, export_way):
        result_way = ""
        if export_way == "print":
            for id in arr_project_id:
                result_way = props.multi_print_url + id + "&ids[]="
            return open_page(result_way)

        elif export_way == "save":
            for id in arr_project_id:
                result_way = props.multi_print_url + id + "&ids[]="
            return open_page(result_way)

        else:
            return 0

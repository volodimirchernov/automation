from Base_methods.Common_methods import *
from Environment.Xpath_library.Xpath_save_as import *


# File list


# delete file on position [1-5]
def delete_document_from_list_method(driver, position):
    delete_file_Element = driver.find_element_by_xpath(choose_element_position(positionable_delete_file_button_Xpath, position))
    delete_file_Element.click()
    return True


# click view document on position [1-5]
def click_view_document_method(driver, position):
    view_document_Element = driver.find_element_by_xpath(choose_element_position(positionable_view_file_button_Xpath, position))
    view_document_Element.click()
    return True


# Select Pages & Preview


# click on preview tab
def click_preview_method(driver):
    preview_Element = driver.find_element_by_xpath(preview_icon_Xpath)
    preview_Element.click()
    return True


from Base_methods.Common_methods import *
from Environment.Xpath_library.Export.Xpath_common import *

# --- File list


# delete file on position [1-5]
def delete_document_from_list(driver, position):
    delete_file_Element = driver.find_element_by_xpath(choose_element_position(positionable_delete_file_button_Xpath, position))
    return delete_file_Element.click()


# click view document on position [1-5]
def click_view_document(driver, position):
    view_document_Element = driver.find_element_by_xpath(choose_element_position(positionable_view_file_button_Xpath, position))
    return view_document_Element.click()


# --- Select Pages & Preview


# click on preview tab
def click_preview(driver):
    preview_Element = driver.find_element_by_xpath(preview_icon_Xpath)
    return preview_Element.click()


# --- Action toolbar


# click on Save as button
def click_save_as(driver):
    save_as_button_Element = driver.find_element_by_xpath(save_as_button_Xpath)
    return save_as_button_Element.click()

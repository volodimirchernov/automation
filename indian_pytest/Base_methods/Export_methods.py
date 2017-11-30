from Base_methods.Common_methods import *
from Environment.Xpath_library.Export.Xpath_common import *

# --- File list


# delete file on position [1-5]
def delete_document_from_list(self, driver, position):
    delete_file_Element = driver.find_element_by_xpath(choose_element_position(positionable_delete_file_button_Xpath, position))
    click_button(self, driver, delete_file_Element)
    return True


# click view document on position [1-5]
def click_view_document(self, driver, position):
    view_document_Element = driver.find_element_by_xpath(choose_element_position(positionable_view_file_button_Xpath, position))
    click_button(self, driver, view_document_Element)
    return True


# --- Select Pages & Preview


# click on preview tab
def click_preview(driver):
    preview_Element = driver.find_element_by_xpath(preview_icon_Xpath)
    click_button(self, driver, preview_Element)
    return True


# --- Action toolbar


# click on Save as button
def click_save_as(driver):
    save_as_button_Element = driver.find_element_by_xpath(save_as_button_Xpath)
    click_button(self, driver, save_as_button_Element)
    return True

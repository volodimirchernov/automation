from Environment.Xpath_library import Xpath_my_docs as md
from Base_methods.Common_methods import *

# Choose any file in file list

def chooseFilesInMyDocs(driver):
    first_full_document_item_Element = driver.find_element_by_xpath(md.firstFile_checkBox_Xpath)
    second_document_checkbox_Element = driver.find_element_by_xpath(md.secondFile_checkBox_Xpath)
    third_document_checkbox = driver.find_element_by_xpath(md.thirdFile_checkBox_Xpath)

    click_button(driver, first_full_document_item_Element)
    click_button(driver, second_document_checkbox_Element)
    click_button(driver, third_document_checkbox)
    return True


# choose which way of export you need

def choose_export_way(driver, way):
    ways_array = {
                  "print": md.printWay_button_Xpath,
                  "email": md.emailWay_button_Xpath,
                  "sms": md.smsWay_button_Xpath,
                  "fax": md.faxWay_button_Xpath,
                  "save as": md.saveAsWay_button_Xpath
                 }
    # check input
    if way in ways_array:
        correct_way = ways_array[way]
    else:
        return False
    # make action
    export_way = driver.find_element_by_xpath(correct_way)
    click_button(driver, export_way)
    return True

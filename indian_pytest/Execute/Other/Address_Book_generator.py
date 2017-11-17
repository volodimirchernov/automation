import time
from selenium.webdriver import Chrome
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from Base_methods.Export_methods import *
from Base_methods.Mydocs_methods import *
from Base_methods.Home_methods import *


# @pytest.fixture(scope = 'session') - запуск тестов в одной сессии

@pytest.fixture()
def chrome_driver(request):

    # For maximaze (start)

    options = Options()
    options.add_argument("--start-maximized")
    driver = Chrome("C:\\Users\\volodimirQA\\Documents\\GitHub\\automation\\indian_pytest\\Environment\\Drivers\\chromedriver.exe", chrome_options=options)

    # For maximaze (end)

    # Or driver.set_window_size(1200, 800)

    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    #driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


def test_zero(chrome_driver):
    email = "alinachetotam+1@gmail.com"
    contacts_arr = []
    count = 966
    while count != 1001:
        add_email = email.replace("1", str(count))
        contacts_arr.append(add_email)
        count = count + 1

    short_authorize(chrome_driver)
    chrome_driver.get("https://dev5.pdffiller.com/en/export/send/email.htm?id=201527808")
    #chrome_driver.get("https://dev5.pdffiller.com/en/export/send/email.htm?id=201515363")
    time.sleep(6)
    for line in contacts_arr:
        isElement = webdriver.isElementPresent("(.//div[@class='g-form-group']/div[1]/span[1]/div[1]/input)[1]")
        if(isElement):
            print(isElement+" - "+str(isElement))
        chrome_driver.find_element_by_xpath("(.//div[@class='g-form-group']/div[1]/span[1]/div[1]/input)[1]").click()
        chrome_driver.find_element_by_xpath("(.//div[@class='g-form-group']/div[1]/span[1]/div[1]/input)[1]").send_keys(line)
        chrome_driver.find_element_by_xpath("(.//span[@class='g-form-add-contact'])[1]").click()
        time.sleep(1)
        chrome_driver.find_element_by_xpath("(.//a[@class='ReactTags__remove'])[1]").click()
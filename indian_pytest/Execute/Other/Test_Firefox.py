from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
firefox_capabilities['binary'] = 'C:\\Users\\vchernov\\Desktop\\drivers\\geckodriver.exe'
browser = webdriver.Firefox(capabilities=firefox_capabilities)
browser.get('https://www.google.com')

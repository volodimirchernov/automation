from selenium import webdriver

browser = webdriver.Firefox("../Environment/Drivers/geckodriver.exe")
browser.get('https://www.google.com')
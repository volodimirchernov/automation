# Need for this - pip install webdriver_manager
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import Firefox, DesiredCapabilities
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeDriverManager, IEDriverManager
from webdriver_manager.phantomjs import PhantomJsDriverManager


DesiredCapabilities = {}
DesiredCapabilities['platform'] = 'WINDOWS'
DesiredCapabilities['browserName'] = 'Firefox'
DesiredCapabilities['browserName'] = 'GoogleChrome'
DesiredCapabilities['browserName'] = 'Edge'
DesiredCapabilities['browserName'] = 'IE'

# Chrome 62

#driver = webdriver.Chrome(ChromeDriverManager().install())


# Firefox 56

#binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
#driver = webdriver.Firefox(firefox_binary=binary, executable_path=GeckoDriverManager().install())


# Edge 15

#dir = "C:\\Users\\vchernov\\Documents\\GitHub\\automation\\indian_pytest\\Environment\\Drivers\\edgedriver.exe"
#edge_path = dir + "/MicrosoftWebDriver"
#driver = webdriver.Edge(executable_path=dir)
#driver = webdriver.Edge(EdgeDriverManager().install())


# IE11

#capabilities = DesiredCapabilities.INTERNETEXPLORER
#capabilities["platform"] = "windows"
#capabilities["browserName"] = "internet explorer"
#capabilities["ignoreProtectedModeSettings"] = True
#capabilities["IntroduceInstabilityByIgnoringProtectedModeSettings"] = True
#capabilities["nativeEvents"] = True
#capabilities["ignoreZoomSetting"] = True
#capabilities["requireWindowFocus"] = True
#capabilities["INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS"] = True
#driver = webdriver.Ie(executable_path=IEDriverManager().install())

#driver = webdriver.Ie(IEDriverManager().install())


# Phantom JS

driver = webdriver.PhantomJS(PhantomJsDriverManager().install())
driver.get("https://tproger.ru/")
driver.close()
driver.quit()
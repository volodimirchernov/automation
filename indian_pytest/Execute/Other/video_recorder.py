from webbrowser import Chrome

from test_recorder.decorator import video

driver = Chrome("../Environment/Drivers/chromedriver.exe")

@video()
def test_selene_demo(self):
    driver.get("www.google.com")
import mathlib
from selenium.webdriver import Chrome
import pytest
import sys

# @pytest.fixture(scope = 'session') - запуск тестов в одной сессии

@pytest.fixture()
def webdriver(request):
    driver = Chrome("C:\\Users\\volodimirQA\\Desktop\\drivers\\chromedriver.exe")
    driver.implicitly_wait(20)
    driver.set_page_load_timeout(20)
    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver


def test_one(webdriver):
    webdriver.get("https://dev5.pdffiller.com/")
    assert True

def test_second(webdriver):
    webdriver.get("https://www.pdffiller.com/")
    assert True








# @pytest.mark.skipif(sys.version_info < (2, 5), reason="i don't need this shit")
# def test_calc_total(test):
#   total = mathlib.calc_total(4, 5)
#  assert total == 9


# import mathlib


# @pytest.mark.chrome
# def test_calc_multiply(test):
#   total = mathlib.calc_multiply(4, 5)
#  assert total == 20



# запуск всех тестов, имеющих в имени word - pytest -k word
# запуск по маркировке
# @pytest.mark.word перед методом
# команда в консоль - pytest -m word

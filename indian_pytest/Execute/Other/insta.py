import time
from selenium.webdriver import Chrome
import io
import pytest

# Открываем файл

f = open("../Environment/tags.csv", "tr", encoding="utf-8")

# список для хранения тегов для поиска

tags_arr = []
result_arr = []

# цикл заполнения списка тегами из файла

for line in f:
    tags_arr.append(line)

# закрываем файл

f.close()

# Выполнения скрипта в Chrome

driver = Chrome("../Environment/Drivers/chromedriver.exe")
driver.implicitly_wait(20)
driver.set_page_load_timeout(20)
driver.maximize_window()

driver.get("https://www.instagram.com/explore/")
driver.find_element_by_xpath(".//input[@aria-label='Номер телефона, имя пользователя или эл. адрес']").send_keys("volodimirchernov@gmail.com")
driver.find_element_by_xpath(".//input[@type='password']").send_keys("050903Crash")

driver.find_element_by_xpath(".//button").click()

# Пройдена авторизация

time.sleep(5)

# метод для обработки тегов

def use_tag(current_tag):
#    time.sleep(5)
    driver.find_element_by_xpath(".//nav[@role='navigation']/div[2]/div/div/div[2]").click()
    search = driver.find_element_by_xpath(".//nav[@role='navigation']/div[2]/div/div/div[2]/input")
    search.clear()
    search.send_keys("#" + current_tag)
    time.sleep(1)

    tag_count = driver.find_elements_by_xpath(".//nav[@role='navigation']/div[2]/div/div/div/div/div/div/a/div/div/div")
    #post_count = driver.find_elements_by_xpath(".//nav[@role='navigation']/div[2]/div/div/div/div/div/div/a/div/div/div[2]/span/span")

    #print(len(tag_count))
    max_a = len(tag_count)

    i = 0
    while i < max_a:
        # print(tag_count[i].text + " - " + tag_count[i+1].text)
        posts_text = tag_count[i + 1].text
        posts_text.replace(" публикаций", "")
        gg = posts_text[:-10]
        gg.rstrip()
        if len(gg) == 8:
            result_arr.append(tag_count[i].text + " - " + gg)
        i = i+2


for tag_element in tags_arr:
    print("\n ---Следующий тег: " + tag_element)
# цикличное использование маетода для разных тегов
    use_tag(tag_element)


# запись в файл собранных результатов


with io.open("../Environment/results.csv", "tw", encoding="utf-8") as f:
    for line in result_arr:
        f.write(line + "\n")

f.close()


driver.close()

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
#     Открыть страницу https://suninjuly.github.io/selects1.html
    browser.get(link)

#     Посчитать сумму заданных чисел
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)

#     Выбрать в выпадающем списке значение равное расчитанной сумме
    print(num1+num2)
    # browser.find_element(By.ID, "dropdown").click()
    # browser.find_element(By.CSS_SELECTOR, "[value='{}']".format(num1+num2)).click()

    # # select
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(num1+num2))

#     Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
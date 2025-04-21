from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    x_value = browser.find_element(By.CSS_SELECTOR, "#input_value") 
    x = x_value.text
    input1.send_keys(calc(x))
    button1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    button1.click()
    button2 = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    button2.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()
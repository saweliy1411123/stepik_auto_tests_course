import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # browser.execute_script('document.title="Script executing";')
    browser.get(link)
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    print(checkbox.text)
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    print(radiobutton.text)
    radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit'")
    print(button.text)
    button.click()

finally:
    time.sleep(10)
    browser.quit()
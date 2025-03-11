from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radiobtn = browser.find_element(By.ID, "robotsRule")
    radiobtn.click()
    
    input = browser.find_element(By.ID, "answer")

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))

    input.send_keys(y)

    btn = browser.find_element(By.CLASS_NAME, "btn")
    btn.click()

finally:
    time.sleep(10)
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

url = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element(By.CLASS_NAME, "btn").click()

    browser.switch_to.alert.accept()

    time.sleep(1)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    browser.find_element(By.CLASS_NAME, "btn").click()
    
finally:
    time.sleep(10)
    browser.quit()
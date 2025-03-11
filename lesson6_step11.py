from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "http://suninjuly.github.io/registration1.html"
urlNew = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    # Заполнение формы на старой версии
    input_firstname = browser.find_element(By.CLASS_NAME, "form-selector")
    input_firstname.send_keys("First Name")

    input_lastname = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    input_lastname.send_keys("Last Name")
    
    input_email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    input_email.send_keys("test@example.com")

    # Проверяем успешность регистрации
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
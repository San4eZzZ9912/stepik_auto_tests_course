from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_registration(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)

        # Уникальные селекторы для первой страницы
        first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.first_class > input.form-control.first")
        first_name.send_keys("Ivan")
        
        last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.second_class > input.form-control.second")
        last_name.send_keys("Petrov")
        
        email = browser.find_element(By.CSS_SELECTOR, "div.first_block > div.form-group.third_class > input.form-control.third")
        email.send_keys("test@test.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем успешность регистрации
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return "Congratulations! You have successfully registered!" in welcome_text

    finally:
        time.sleep(5)
        browser.quit()

# Тест должен пройти
print("Test registration1 (should pass):", test_registration("http://suninjuly.github.io/registration1.html"))

# Тест должен упасть с NoSuchElementException
try:
    print("Test registration2 (should fail):", test_registration("http://suninjuly.github.io/registration2.html"))
except Exception as e:
    print(f"Test registration2 failed as expected with error: {type(e).__name__}")
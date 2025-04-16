from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем браузер
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    # 1. Заполняем текстовые поля
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")

    # 2. Создаем временный текстовый файл
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Получаем путь к текущей директории
    file_name = "example.txt"
    file_path = os.path.join(current_dir, file_name)  # Формируем полный путь к файлу

    with open(file_path, "w") as f:  # Создаем файл
        f.write("This is a test file.")  # Можно оставить пустым

    # 3. Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(file_path)

    # 4. Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Удаляем временный файл после завершения
    if os.path.exists(file_path):
        os.remove(file_path)

    # Успеваем скопировать код за 10 секунд
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла

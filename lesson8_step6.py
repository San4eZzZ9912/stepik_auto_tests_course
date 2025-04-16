from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

# Функция для вычисления значения функции
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # Открываем браузер
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # 1. Нажимаем на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    button.click()

    # 2. Переключаемся на новую вкладку
    new_window = browser.window_handles[1]  # Получаем дескриптор новой вкладки
    browser.switch_to.window(new_window)    # Переключаемся на новую вкладку

    # 3. Решаем капчу на новой странице
    # Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # Вычисляем значение функции
    y = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку "Submit"
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:
    # Успеваем скопировать код за 10 секунд
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла

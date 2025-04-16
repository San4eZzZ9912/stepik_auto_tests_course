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
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # 1. Считываем значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 2. Вычисляем значение функции
    y = calc(x)

    # 3. Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 4. Прокручиваем страницу до чекбокса и отмечаем его
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()

    # 5. Прокручиваем страницу до радиокнопки и выбираем её
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # 6. Прокручиваем страницу до кнопки и нажимаем её
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    # Успеваем скопировать код за 10 секунд
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()

# Не забываем оставить пустую строку в конце файла

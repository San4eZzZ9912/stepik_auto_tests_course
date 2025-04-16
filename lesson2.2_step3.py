from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    # Можно тестировать на любой из этих страниц
    browser.get("https://suninjuly.github.io/selects1.html")
    # browser.get("https://suninjuly.github.io/selects2.html")

    # Находим числа и вычисляем их сумму
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    sum_result = str(int(num1) + int(num2))

    # Выбираем значение в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_result)

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # Даем время скопировать код
    time.sleep(10)
    browser.quit()
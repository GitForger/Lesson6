from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    # Шаг 1: Перейдите на сайт
    driver.get("http://uitestingplayground.com/textinput")
    print("Страница загружена")
    
    wait = WebDriverWait(driver, 10)
    
    # Шаг 2: Укажите в поле ввода текст SkyPro
    input_field = wait.until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")
    print("Текст 'SkyPro' введен в поле")
    
    # Шаг 3: Нажмите на синюю кнопку
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    print("Синяя кнопка нажата")
    
    # Ждем обновления текста кнопки
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    
    # Шаг 4: Получите текст кнопки и выведите в консоль
    button_text = blue_button.text
    print(f"Текст кнопки: '{button_text}'")

finally:
    time.sleep(5)
    driver.quit()
    print("Браузер закрыт")

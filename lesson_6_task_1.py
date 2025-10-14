from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    print("Страница загружена")
    
    # Увеличиваем время ожидания до 20 секунд
    wait = WebDriverWait(driver, 20)
    
    # Нажимаем кнопку
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    print("Кнопка нажата - ждем ~15 секунд...")
    
    # Ждем пока появится элемент с классом bg-success
    success_element = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
    )
    print("Зеленая плашка появилась!")
    
    # Получаем текст
    banner_text = success_element.text
    print(f"Текст из плашки: '{banner_text}'")

finally:

    driver.quit()

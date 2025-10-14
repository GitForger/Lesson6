from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    wait = WebDriverWait(driver, 17)
    
    # Ждем пока 4-я картинка (с id="landscape") станет видимой
    fourth_image = wait.until(
        EC.visibility_of_element_located((By.ID, "landscape"))
    )
    
    # Теперь получаем все картинки
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    print(f"Загружено картинок: {len(images)}")
    
    third_image_src = images[2].get_attribute("src")
    print(f"SRC третьей картинки: {third_image_src}")
    

finally:
    driver.quit()

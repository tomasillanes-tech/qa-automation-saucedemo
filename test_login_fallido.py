from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_credenciales_incorrectas(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
    driver.find_element(By.ID, "login-button").click()
    
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))
    
    assert "do not match" in error.text
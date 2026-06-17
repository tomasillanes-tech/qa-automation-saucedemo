from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

wait = WebDriverWait(driver, 10)
elemento_error = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
)

mensaje_error = elemento_error.text
print(f"Mensaje mostrado: {mensaje_error}")

assert "locked out" in mensaje_error
print("✅ El sistema bloqueó correctamente al usuario")

driver.quit()
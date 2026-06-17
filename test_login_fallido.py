from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

# Usuario válido pero contraseña incorrecta
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Busca el mensaje de error que debería aparecer
mensaje_error = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text

# Verifica que el mensaje contiene el texto esperado
assert "Username and password do not match" in mensaje_error
print("✅ El sistema rechazó correctamente las credenciales incorrectas")
print(f"Mensaje mostrado: {mensaje_error}")

driver.quit()
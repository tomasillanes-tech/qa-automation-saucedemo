from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Espera a que cargue la página de productos
wait.until(EC.url_contains("inventory"))

# Agrega el primer producto (mochila) al carrito
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Verifica que el ícono del carrito muestra "1"
contador_carrito = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
assert contador_carrito == "1"
print(f"✅ Producto agregado correctamente. Carrito muestra: {contador_carrito}")

# Hace clic en el carrito para verificar que el producto está ahí
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
wait.until(EC.url_contains("cart"))

nombre_producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
assert nombre_producto == "Sauce Labs Backpack"
print(f"✅ Producto correcto en el carrito: {nombre_producto}")

driver.quit()
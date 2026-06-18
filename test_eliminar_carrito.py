from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_eliminar_producto_del_carrito(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    # Agregar producto al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Verifica que el carrito muestra "1"
    contador = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert contador == "1"
    print(f"✅ Producto agregado. Carrito muestra: {contador}")

    # Elimina el producto (el botón ahora dice "Remove")
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    # Verifica que el badge del carrito ya no existe
    badges = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert len(badges) == 0
    print("✅ Producto eliminado correctamente. El carrito está vacío")
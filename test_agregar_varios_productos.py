from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_varios_productos_al_carrito(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    # Agregar 3 productos distintos
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Verifica que el contador del carrito muestra "3"
    contador = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text
    assert contador == "3"
    print(f"✅ Contador del carrito correcto: {contador}")

    # Va al carrito
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    # Obtiene los nombres de los productos en el carrito
    nombres_en_carrito = [
        el.text for el in driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
    ]

    print(f"Productos en el carrito: {nombres_en_carrito}")

    # Verifica que están los 3 productos esperados
    assert len(nombres_en_carrito) == 3
    assert "Sauce Labs Backpack" in nombres_en_carrito
    assert "Sauce Labs Bike Light" in nombres_en_carrito
    assert "Sauce Labs Bolt T-Shirt" in nombres_en_carrito

    print("✅ Los 3 productos esperados están en el carrito")
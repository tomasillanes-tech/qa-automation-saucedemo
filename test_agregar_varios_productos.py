from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_varios_productos_al_carrito(driver):
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    badge = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
    assert badge.text == "3"

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item_name")))
    nombres_en_carrito = [
        el.text for el in driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")
    ]

    assert len(nombres_en_carrito) == 3
    assert "Sauce Labs Backpack" in nombres_en_carrito
    assert "Sauce Labs Bike Light" in nombres_en_carrito
    assert "Sauce Labs Bolt T-Shirt" in nombres_en_carrito
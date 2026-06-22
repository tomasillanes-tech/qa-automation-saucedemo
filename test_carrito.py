from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_agregar_producto_al_carrito(driver):
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    badge = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
    assert badge.text == "1"

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    nombre_producto = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".inventory_item_name"))
    ).text
    assert nombre_producto == "Sauce Labs Backpack"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_completo(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    # Agregar producto al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Ir al carrito
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    # Iniciar checkout
    driver.find_element(By.ID, "checkout").click()
    wait.until(EC.url_contains("checkout-step-one"))

    # Llenar formulario de datos
    driver.find_element(By.ID, "first-name").send_keys("Tomas")
    driver.find_element(By.ID, "last-name").send_keys("Illanes")
    driver.find_element(By.ID, "postal-code").send_keys("2510000")
    driver.find_element(By.ID, "continue").click()

    # Verifica que llegamos a la pantalla de resumen
    wait.until(EC.url_contains("checkout-step-two"))
    assert "checkout-step-two" in driver.current_url
    print("✅ Resumen de compra cargado correctamente")

    # Finalizar la compra
    driver.find_element(By.ID, "finish").click()

    # Verifica el mensaje final de éxito
    mensaje = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".complete-header"))
    ).text

    assert mensaje == "Thank you for your order!"
    print(f"✅ Compra completada con éxito. Mensaje: {mensaje}")
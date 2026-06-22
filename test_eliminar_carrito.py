from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_eliminar_producto_del_carrito(driver):
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    badge = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))
    assert badge.text == "1"

    wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))).click()

    # Espera explícita a que el badge desaparezca del DOM
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))

    badges = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert len(badges) == 0
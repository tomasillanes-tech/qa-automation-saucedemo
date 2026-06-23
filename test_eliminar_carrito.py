from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import click_js

def test_eliminar_producto_del_carrito(driver):
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1")

    btn_remove = wait.until(EC.presence_of_element_located((By.ID, "remove-sauce-labs-backpack")))
    click_js(driver, btn_remove)

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")) == 0)
    badges = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert len(badges) == 0
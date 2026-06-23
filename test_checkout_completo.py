from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import click_js

def test_checkout_completo(driver):
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait.until(lambda d: d.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "1")

    link_carrito = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    click_js(driver, link_carrito)
    wait.until(EC.url_contains("cart"))

    btn_checkout = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    click_js(driver, btn_checkout)
    wait.until(EC.url_contains("checkout-step-one"))

    driver.find_element(By.ID, "first-name").send_keys("Tomas")
    driver.find_element(By.ID, "last-name").send_keys("Illanes")
    driver.find_element(By.ID, "postal-code").send_keys("2510000")
    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two"))
    assert "checkout-step-two" in driver.current_url

    btn_finish = wait.until(EC.presence_of_element_located((By.ID, "finish")))
    click_js(driver, btn_finish)

    mensaje = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".complete-header"))
    ).text
    assert mensaje == "Thank you for your order!"
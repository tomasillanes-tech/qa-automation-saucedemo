from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout_completo(driver):
    wait = WebDriverWait(driver, 10)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping_cart_badge")))

    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
    wait.until(EC.url_contains("cart"))

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.url_contains("checkout-step-one"))

    driver.find_element(By.ID, "first-name").send_keys("Tomas")
    driver.find_element(By.ID, "last-name").send_keys("Illanes")
    driver.find_element(By.ID, "postal-code").send_keys("2510000")
    driver.find_element(By.ID, "continue").click()

    wait.until(EC.url_contains("checkout-step-two"))
    assert "checkout-step-two" in driver.current_url

    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    mensaje = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".complete-header"))
    ).text
    assert mensaje == "Thank you for your order!"
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_usuario_bloqueado(driver):
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='error']")))

    assert "locked out" in error.text
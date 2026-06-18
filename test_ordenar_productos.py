from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def test_ordenar_por_precio_menor_a_mayor(driver):
    wait = WebDriverWait(driver, 10)

    # Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.url_contains("inventory"))

    # Selecciona el dropdown de ordenamiento
    dropdown = Select(driver.find_element(By.CSS_SELECTOR, "[data-test='product-sort-container']"))
    
    # Elige la opción "Price (low to high)"
    dropdown.select_by_value("lohi")

    # Obtiene todos los precios mostrados en la página
    elementos_precio = driver.find_elements(By.CSS_SELECTOR, ".inventory_item_price")
    precios = [float(p.text.replace("$", "")) for p in elementos_precio]

    print(f"Precios en el orden mostrado: {precios}")

    # Verifica que la lista esté efectivamente ordenada de menor a mayor
    assert precios == sorted(precios)
    print("✅ Los productos están ordenados correctamente de menor a mayor precio")
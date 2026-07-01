import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    opciones = Options()
    opciones.add_argument("--headless=new")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    opciones.add_argument("--window-size=1920,1080")

    nav = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opciones
    )
    nav.implicitly_wait(5)
    nav.get("https://www.saucedemo.com/")

    yield nav

    nav.quit()


def click_js(driver, elemento):
    driver.execute_script("arguments[0].click();", elemento)
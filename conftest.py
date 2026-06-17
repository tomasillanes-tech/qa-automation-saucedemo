import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # Esto se ejecuta ANTES de cada test
    nav = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    nav.get("https://www.saucedemo.com/")
    
    yield nav  # Aquí se "pausa" y se ejecuta el test
    
    # Esto se ejecuta DESPUÉS de cada test (limpieza automática)
    nav.quit()
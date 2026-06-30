from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_ordenar_por_precio_menor_a_mayor(page: Page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.ir_a_pagina()
    login_page.iniciar_sesion("standard_user", "secret_sauce")

    inventory_page.ordenar_por("lohi")

    precios = inventory_page.obtener_precios()
    assert precios == sorted(precios)
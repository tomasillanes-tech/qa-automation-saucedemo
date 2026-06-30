from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_exitoso(page: Page):
    login_page = LoginPage(page)
    
    login_page.ir_a_pagina()
    login_page.iniciar_sesion("standard_user", "secret_sauce")
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
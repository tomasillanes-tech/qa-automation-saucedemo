from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_credenciales_incorrectas(page: Page):
    login_page = LoginPage(page)
    
    login_page.ir_a_pagina()
    login_page.iniciar_sesion("standard_user", "clave_incorrecta")
    
    error = login_page.obtener_mensaje_error()
    expect(error).to_contain_text("do not match")
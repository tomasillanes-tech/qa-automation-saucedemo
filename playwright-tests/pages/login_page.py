class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_usuario = "#user-name"
        self.input_password = "#password"
        self.boton_login = "#login-button"
        self.mensaje_error = "[data-test='error']"

    def ir_a_pagina(self):
        self.page.goto("https://www.saucedemo.com/")

    def iniciar_sesion(self, usuario, password):
        self.page.fill(self.input_usuario, usuario)
        self.page.fill(self.input_password, password)
        self.page.click(self.boton_login)

    def obtener_mensaje_error(self):
        return self.page.locator(self.mensaje_error)
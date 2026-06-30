from playwright.sync_api import Page, expect

def test_login_credenciales_incorrectas(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.fill("#user-name", "standard_user")
    page.fill("#password", "clave_incorrecta")
    page.click("#login-button")
    
    error = page.locator("[data-test='error']")
    expect(error).to_contain_text("do not match")
    print("✅ Login fallido detectado correctamente")
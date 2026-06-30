from playwright.sync_api import Page, expect

def test_login_exitoso(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("✅ Login exitoso con Playwright")
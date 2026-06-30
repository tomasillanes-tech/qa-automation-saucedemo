from playwright.sync_api import Page, expect

def test_agregar_producto_al_carrito(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.click("#add-to-cart-sauce-labs-backpack")
    
    badge = page.locator(".shopping_cart_badge")
    expect(badge).to_have_text("1")
    
    page.click(".shopping_cart_link")
    
    nombre_producto = page.locator(".inventory_item_name")
    expect(nombre_producto).to_have_text("Sauce Labs Backpack")
    print("✅ Producto agregado y verificado en el carrito")
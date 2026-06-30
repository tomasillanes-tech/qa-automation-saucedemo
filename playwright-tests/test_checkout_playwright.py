from playwright.sync_api import Page, expect

def test_checkout_completo(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")

    page.click(".shopping_cart_link")
    page.click("#checkout")

    page.fill("#first-name", "Tomas")
    page.fill("#last-name", "Illanes")
    page.fill("#postal-code", "2510000")
    page.click("#continue")

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    page.click("#finish")

    mensaje = page.locator(".complete-header")
    expect(mensaje).to_have_text("Thank you for your order!")
    print("✅ Compra completada con éxito")
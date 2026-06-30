from playwright.sync_api import Page

def test_ordenar_por_precio_menor_a_mayor(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.select_option("[data-test='product-sort-container']", "lohi")

    elementos_precio = page.locator(".inventory_item_price").all_text_contents()
    precios = [float(p.replace("$", "")) for p in elementos_precio]

    print(f"Precios en orden: {precios}")
    assert precios == sorted(precios)
    print("✅ Productos ordenados correctamente por precio")
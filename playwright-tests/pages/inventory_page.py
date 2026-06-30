class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.link_carrito = ".shopping_cart_link"
        self.badge_carrito = ".shopping_cart_badge"
        self.selector_orden = "[data-test='product-sort-container']"
        self.precios_productos = ".inventory_item_price"

    def agregar_producto(self, id_producto):
        self.page.click(f"#add-to-cart-{id_producto}")

    def obtener_badge_carrito(self):
        return self.page.locator(self.badge_carrito)

    def ir_al_carrito(self):
        self.page.click(self.link_carrito)

    def ordenar_por(self, valor):
        self.page.select_option(self.selector_orden, valor)

    def obtener_precios(self):
        textos = self.page.locator(self.precios_productos).all_text_contents()
        return [float(p.replace("$", "")) for p in textos]
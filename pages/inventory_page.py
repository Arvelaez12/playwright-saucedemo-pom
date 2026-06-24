class InventoryPage:
    def __init__(self, page):
        """
        Controla el catálogo de productos y el encabezado global de la tienda.
        """
        self.page = page
        
        # --- LOCALIZADORES ---
        self.title_span = "span.title"
        self.shopping_cart_badge = "span.shopping_cart_badge"
        
        # SELECTOR AVANZADO RELACIONAL:
        # Le decimos: Busca el contenedor del inventario (.inventory_item) que ADENTRO 
        # tenga el texto de la mochila, y de ahí busca su botón que dice "Add to cart".
        self.backpack_container_btn = (
            "div.inventory_item:has-text('Sauce Labs Backpack') >> button:has-text('Add to cart')"
        )

    # --- ACCIONES ---
    def obtener_titulo_de_pagina(self):
        """Retorna el texto del encabezado."""
        return self.page.locator(self.title_span).inner_text()

    def agregar_mochila_al_carrito(self):
        """Hace clic en el botón usando nuestro selector relacional inteligente."""
        self.page.click(self.backpack_container_btn)

    def obtener_contador_del_carrito(self):
        """Retorna el número que aparece en el ícono del carrito."""
        return self.page.locator(self.shopping_cart_badge).inner_text()
class CheckoutPage:
    def __init__(self, page):
        """
        Controla la pantalla del carrito y el formulario de envío (Checkout).
        """
        self.page = page

        # --- LOCALIZADORES DE LA PÁGINA ---
        # 1. El botón con forma de carrito de compras en la esquina superior
        self.cart_icon = "a.shopping_cart_link"
        
        # 2. El botón que inicia el proceso de pago adentro del carrito
        self.checkout_button = "button#checkout"
        
        # 3. Los tres campos del formulario de datos personales
        self.first_name_input = "input#first-name"
        self.last_name_input = "input#last-name"
        self.postal_code_input = "input#postal-code"
        
        # 4. El botón "Continue" que procesa los datos ingresados
        self.continue_button = "input#continue"
        
        # 5. El texto del encabezado en la pantalla de confirmación final
        self.sub_title_span = "span.title"

    # --- ACCIONES (MÉTODOS) ---
    def ir_al_carrito_e_iniciar_pago(self):
        """Hace clic en el ícono del carrito y luego presiona 'Checkout'."""
        self.page.click(self.cart_icon)
        self.page.click(self.checkout_button)

    def llenar_formulario_envio(self, nombre, apellido, codigo_postal):
        """
        Recibe tres textos dinámicos y los teclea en sus respectivos campos,
        para luego presionar el botón de continuar.
        """
        self.page.fill(self.first_name_input, nombre)
        self.page.fill(self.last_name_input, apellido)
        self.page.fill(self.postal_code_input, codigo_postal)
        self.page.click(self.continue_button)

    def obtener_subtitulo_confirmacion(self):
        """Retorna el texto superior (Ej: 'Checkout: Overview') para validar el éxito."""
        return self.page.locator(self.sub_title_span).inner_text()
class LoginPage:
    def __init__(self, page):
        """
        El constructor recibe la instancia del navegador (page).
        Aquí centralizamos todos los localizadores de la pantalla de Login.
        Si un desarrollador cambia un ID mañana, solo lo editas aquí.
        """
        self.page = page
        
        # --- LOCALIZADORES ROBUSTOS ---
        self.username_input = "input#user-name"
        self.password_input = "input#password"
        self.login_button = "input#login-button"
        self.error_message_container = "h3[data-test='error']"

    # --- ACCIONES / MÉTODOS DE LA PÁGINA ---
    def navegar_a_login(self, base_url):
        """Abre el navegador directo en la URL de SauceDemo."""
        self.page.goto(base_url)

    def ingresar_credenciales(self, usuario, contrasena):
        """Escribe en los campos correspondientes."""
        self.page.fill(self.username_input, usuario)
        self.page.fill(self.password_input, contrasena)

    def hacer_clic_en_login(self):
        """Presiona el botón de inicio de sesión."""
        self.page.click(self.login_button)

    def obtener_texto_de_error(self):
        """Retorna el texto de alerta si las credenciales fallan."""
        return self.page.locator(self.error_message_container).inner_text()
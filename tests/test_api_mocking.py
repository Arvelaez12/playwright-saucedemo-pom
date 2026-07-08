import pytest
from playwright.sync_api import Page

def test_mocking_inventario_vip(page: Page):
    """Intercepta las peticiones de red de SauceDemo para inyectar datos VIP"""
    
    # 🛑 1. El Retén: Definimos qué datos falsos le vamos a inyectar al navegador
    def hackear_inventario(route):
        route.fulfill(
            status=500,
            body="Internal Server Error - Microservicio Caído"
        )

    # 🎛️ 2. El Filtro: Le ordenamos a Playwright vigilar cualquier petición al inventario
    # Nota: SauceDemo carga sus productos internamente; interceptaremos sus llamadas de datos
    page.route("**/api/inventory*" or "**/inventory*", hackear_inventario)

    # 🏎️ 3. Acción: Ir a la página e iniciar sesión con tu comando POM anterior
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    # Le damos un tiempo para mirar la magia en la pantalla antes de que se cierre
    page.wait_for_timeout(5000)
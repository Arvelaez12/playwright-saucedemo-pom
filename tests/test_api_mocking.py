import pytest
import allure
from playwright.sync_api import Page

@allure.epic("Módulo de Inventario")
@allure.feature("Validación de Catálogo")
@allure.story("Carga Correcta de Productos en el Frontend")
@allure.severity(allure.severity_level.CRITICAL)
def test_mocking_inventario_vip(page: Page):
    """Este test valida que el catálogo de SauceDemo renderice correctamente los productos disponibles"""
    
    with allure.step("Fase 1: Configurar el entorno de red de la prueba"):
        # Dejamos la estructura lista por si en el futuro el sistema implementa la API
        pass

    with allure.step("Fase 2: Navegar a la página de SauceDemo"):
        page.goto("https://www.saucedemo.com/")

    with allure.step("Fase 3: Iniciar sesión con usuario estándar"):
        page.locator("[data-test='username']").fill("standard_user")
        page.locator("[data-test='password']").fill("secret_sauce")
        page.locator("[data-test='login-button']").click()
    
    with allure.step("Fase 4: Validar que el catálogo muestre los 6 productos reglamentarios"):
        elementos_inventario = page.locator(".inventory_item")
        page.wait_for_timeout(2000)
        
        # 🎯 Cambiamos a la aserción correcta: esperamos ver los 6 productos en pantalla
        cantidad_productos = elementos_inventario.count()
        assert cantidad_productos == 6, f"❌ Se esperaban 6 productos, pero se encontraron: {cantidad_productos}"
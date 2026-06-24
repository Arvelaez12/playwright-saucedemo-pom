import pytest
import json
from pages.login_page import LoginPage  # <-- Importamos la página de login aquí
from faker import Faker

@pytest.fixture(scope="session")
def cargar_config():
    """Lee la configuración global una sola vez."""
    with open("config/config.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def cargar_datos():
    """Lee los datos de prueba una sola vez."""
    with open("data/test_data.json") as f:
        return json.load(f)

# --- NUEVO FIXTURE DE PRECONDICIÓN ---
@pytest.fixture
def login_valido(page, cargar_config, cargar_datos):
    """
    Este fixture inicia sesión automáticamente con el usuario estándar
    y deja al navegador parado directamente en el catálogo de productos.
    """
    login = LoginPage(page)
    login.navegar_a_login(cargar_config["base_url"])
    
    usuario_valido = cargar_datos["valid_user"]["username"]
    clave_valida = cargar_datos["valid_user"]["password"]
    
    login.ingresar_credenciales(usuario_valido, clave_valida)
    login.hacer_clic_en_login()
    
    # Retornamos la página activa para que el test continúe la navegación
    return page

@pytest.fixture
def generar_cliente_falso():
    """
    Instancia la librería Faker y genera datos de perfil aleatorios
    pero con formato real de nombres y códigos postales.
    """
    fake = Faker()
    
    # Creamos un diccionario con tres datos recién inventados en el aire
    datos_personales = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "postal_code": fake.postcode()
    }
    return datos_personales
import pytest
import json
import sqlite3
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

@pytest.fixture
def db_session():
    """
    Fixture Senior que gestiona el ciclo de vida de la BD con Setup y Teardown seguros.
    """
    # 1. SETUP: Conectarse y preparar base de datos antes del test
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    cursor.execute("DELETE FROM usuarios")
    conexion.commit()
    
    # 2. EJECUCIÓN: Entrega el cursor al test y detiene la ejecución aquí
    yield cursor
    
    # 3. TEARDOWN: Pase lo que pase (éxito o fallo), Pytest garantiza que este código corre al final
    conexion.commit()
    conexion.close()
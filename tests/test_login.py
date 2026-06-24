from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

# ==========================================================
# PRUEBA 1: LOGIN FALLIDO (No usa precondición, prueba el login mismo)
# ==========================================================
def test_login_fallido_credenciales_invalidas(page, cargar_config, cargar_datos):
    login = LoginPage(page)
    login.navegar_a_login(cargar_config["base_url"])
    
    usuario_incorrecto = cargar_datos["invalid_user"]["username"]
    clave_incorrecta = cargar_datos["invalid_user"]["password"]
    login.ingresar_credenciales(usuario_incorrecto, clave_incorrecta)
    login.hacer_clic_en_login()

    mensaje_error_visible = login.obtener_texto_de_error()
    mensaje_esperado = "Epic sadface: Username and password do not match any user in this service"
    assert mensaje_error_visible == mensaje_esperado, f"Error: Se esperaba '{mensaje_esperado}' pero se obtuvo '{mensaje_error_visible}'"


# ==========================================================
# PRUEBA 2: LOGIN EXITOSO (¡Ahora usa el fixture login_valido!)
# ==========================================================
def test_login_exitoso(login_valido):
    # 'login_valido' ya hizo el login en secreto. Aquí solo validamos el resultado.
    inventory = InventoryPage(login_valido)
    
    titulo_actual = inventory.obtener_titulo_de_pagina()
    titulo_esperado = "Products"
    assert titulo_actual == titulo_esperado, f"Error: Se esperaba estar en '{titulo_esperado}' pero el título es '{titulo_actual}'"


# ==========================================================
# PRUEBA 3: AGREGAR PRODUCTO AL CARRITO
# ==========================================================
def test_agregar_producto_al_carrito(login_valido):
    inventory = InventoryPage(login_valido)

    # El navegador ya arranca logueado en la tienda gracias al fixture
    inventory.agregar_mochila_al_carrito()
    cantidad_en_carrito = inventory.obtener_contador_del_carrito()

    cantidad_esperada = "1"
    assert cantidad_en_carrito == cantidad_esperada, f"Error: Se esperaba '{cantidad_esperada}' artículo, pero dice '{cantidad_en_carrito}'"


# ==========================================================
# PRUEBA 4: FLUJO COMPLETO DE CHECKOUT (DATOS ALEATORIOS CON FAKER)
# ==========================================================
def test_flujo_completo_checkout(login_valido, generar_cliente_falso): # <-- Cambiamos 'cargar_datos' por 'generar_cliente_falso'
    inventory = InventoryPage(login_valido)
    checkout = CheckoutPage(login_valido)

    # 1. Acciones directas de negocio
    inventory.agregar_mochila_al_carrito()
    checkout.ir_al_carrito_e_iniciar_pago()

    # 2. Rellenar datos aleatorios generados en tiempo real por Faker
    nombre_cliente = generar_cliente_falso["first_name"]
    apellido_cliente = generar_cliente_falso["last_name"]
    cp_cliente = generar_cliente_falso["postal_code"]
    
    checkout.llenar_formulario_envio(nombre_cliente, apellido_cliente, cp_cliente)

    # 3. Validación de estado final
    subtitulo_actual = checkout.obtener_subtitulo_confirmacion()
    subtitulo_esperado = "Checkout: Overview"
    assert subtitulo_actual == subtitulo_esperado, f"Error: Se esperaba estar en '{subtitulo_esperado}' pero dice '{subtitulo_actual}'"
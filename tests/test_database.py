import pytest

def test_verificar_insercion_en_base_de_datos(db_session):
    # 1. Usamos el cursor provisto automáticamente por el fixture
    cursor = db_session
    
    # 2. Insertar un registro usando SQL puro
    nombre_prueba = "Carlos QA"
    email_prueba = "carlos@testing.com"
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre_prueba, email_prueba))
    
    # El commit y cierre físico de la conexión lo delegamos automáticamente al fixture al terminar.
    
    # 3. PRUEBA DE AUTOMATIZACIÓN: Consultar el dato para verificarlo
    cursor.execute("SELECT nombre, email FROM usuarios WHERE email = ?", (email_prueba,))
    resultado = cursor.fetchone() # Trae el primer registro que coincida
    
    # 4. VALIDACIONES: Comprobar que el registro no sea nulo y tenga los datos correctos
    assert resultado is not None, "Error: El usuario no fue encontrado en la base de datos"
    
    nombre_en_bd, email_en_bd = resultado
    assert nombre_en_bd == nombre_prueba, f"Se esperaba {nombre_prueba} pero se obtuvo {nombre_en_bd}"
    assert email_en_bd == email_prueba, f"Se esperaba {email_prueba} pero se obtuvo {email_en_bd}"
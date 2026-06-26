import pytest
import sqlite3 # Librería nativa de Python para bases de datos SQL

def test_verificar_insercion_en_base_de_datos():
    # 1. Conectarse a la base de datos (si el archivo no existe, Python lo crea automáticamente)
    conexion = sqlite3.connect("tienda.db")
    
    # El cursor es el "puntero" que nos permite escribir y ejecutar comandos SQL
    cursor = conexion.cursor()
    
    # 2. Crear una tabla de prueba limpia
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    
    # Limpiamos la tabla por si acaso corremos el test varias veces
    cursor.execute("DELETE FROM usuarios")
    
    # 3. Insertar un registro usando SQL puro
    nombre_prueba = "Carlos QA"
    email_prueba = "carlos@testing.com"
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre_prueba, email_prueba))
    
    # Guardar los cambios físicamente en el archivo de la base de datos
    conexion.commit()
    
    # 4. PRUEBA DE AUTOMATIZACIÓN: Consultar el dato para verificarlo
    cursor.execute("SELECT nombre, email FROM usuarios WHERE email = ?", (email_prueba,))
    resultado = cursor.fetchone() # Trae el primer registro que coincida
    
    # Cerramos la conexión de forma limpia
    conexion.close()
    
    # 5. VALIDACIONES: Comprobar que el registro no sea nulo y tenga los datos correctos
    assert resultado is not None, "Error: El usuario no fue encontrado en la base de datos"
    
    nombre_en_bd, email_en_bd = resultado
    assert nombre_en_bd == nombre_prueba, f"Se esperaba {nombre_prueba} pero se obtuvo {nombre_en_bd}"
    assert email_en_bd == email_prueba, f"Se esperaba {email_prueba} pero se obtuvo {email_en_bd}"
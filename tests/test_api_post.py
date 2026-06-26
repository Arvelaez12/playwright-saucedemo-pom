import pytest

def test_crear_nuevo_post(playwright):
    # 1. Creamos el contexto del cliente de API
    contexto_api = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    
    # 2. Definimos los datos del nuevo artículo que queremos registrar (Payload)
    nuevo_post_payload = {
        "title": "Automatizacion con Playwright",
        "body": "Aprendiendo a realizar mutacion de datos usando peticiones POST",
        "userId": 99
    }
    
    # 3. Realizamos la peticion POST enviando el diccionario dentro del argumento 'data'
    respuesta = contexto_api.post("/posts", data=nuevo_post_payload)
    
    # 4. VALIDACIÓN 1: El código de estado debe ser 201 (Created)
    assert respuesta.status == 201, f"Error: Se esperaba estado 201 pero se obtuvo {respuesta.status}"
    
    # 5. Extraemos el JSON de respuesta que nos devuelve el servidor
    datos_respuesta = respuesta.json()
    
    # 6. VALIDACIÓN 2: Confirmar que el servidor nos asignó un ID de recurso único
    assert "id" in datos_respuesta, "El servidor no devolvió un campo 'id' para el recurso creado"
    
    # 7. VALIDACIÓN 3: Verificar que los datos guardados coincidan exactamente con lo enviado
    assert datos_respuesta["title"] == nuevo_post_payload["title"]
    assert datos_respuesta["body"] == nuevo_post_payload["body"]
    assert datos_respuesta["userId"] == nuevo_post_payload["userId"]
    
    # Cerramos el contexto limpiamente
    contexto_api.dispose()
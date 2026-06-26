import pytest

# URL Base para nuestro cliente de API
URL_BASE = "https://jsonplaceholder.typicode.com"

def test_actualizar_post_con_put(playwright):
    contexto_api = playwright.request.new_context(base_url=URL_BASE)
    
    # 1. Definimos los nuevos datos que van a reemplazar al Post ID 1
    payload_actualizacion = {
        "id": 1,
        "title": "Titulo Modificado por Alberto",
        "body": "Este cuerpo ha sido actualizado usando un metodo PUT automatizado",
        "userId": 1
    }
    
    # 2. Ejecutamos la peticion PUT apuntando especificamente al recurso /posts/1
    respuesta = contexto_api.put("/posts/1", data=payload_actualizacion)
    
    # 3. VALIDACIÓN: Comprobar el estado exitoso 200 OK
    assert respuesta.status == 200, f"Error en PUT: Se esperaba 200 pero dio {respuesta.status}"
    
    datos_json = respuesta.json()
    
    # 4. VALIDACIÓN: Verificar que los datos cambiaron en el servidor ficticio
    assert datos_json["title"] == payload_actualizacion["title"]
    assert datos_json["body"] == payload_actualizacion["body"]
    
    contexto_api.dispose()


def test_eliminar_post_con_delete(playwright):
    contexto_api = playwright.request.new_context(base_url=URL_BASE)
    
    # 1. Ejecutamos la peticion DELETE directamente sobre el Post ID 1
    respuesta = contexto_api.delete("/posts/1")
    
    # 2. VALIDACIÓN: Comprobar que el servidor acepto la orden (200 OK)
    assert respuesta.status == 200, f"Error en DELETE: Se esperaba 200 pero dio {respuesta.status}"
    
    # 3. VALIDACIÓN: JSONPlaceholder devuelve el objeto vacio {} al eliminar
    datos_json = respuesta.json()
    assert len(datos_json) == 0, f"Se esperaba un objeto vacio pero se recibio: {datos_json}"
    
    contexto_api.dispose()
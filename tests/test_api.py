import pytest

def test_consultar_post_por_id(playwright):
    # 1. Creamos el cliente apuntando a un servidor de pruebas 100% abierto y amigable
    contexto_api = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
    
    # 2. Hacemos la petición GET para traer el post número 1
    respuesta = contexto_api.get("/posts/1")
    
    # 3. VALIDACIÓN 1: El código de estado debe ser 200 OK (Exitoso)
    assert respuesta.status == 200, f"Error: Se esperaba estado 200 pero se obtuvo {respuesta.status}"
    
    # 4. Extraemos los datos en formato JSON
    datos_json = respuesta.json()
    
    # 5. VALIDACIÓN 2: Verificar que el "title" del post contenga el texto esperado
    titulo_actual = datos_json["title"]
    # El post 1 de este servicio público siempre contiene estas palabras iniciales:
    assert "sunt aut facere" in titulo_actual, f"El título obtenido fue: {titulo_actual}"
    
    # Cerramos el contexto de forma limpia
    contexto_api.dispose()
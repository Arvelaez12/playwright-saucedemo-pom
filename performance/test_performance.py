from locust import HttpUser, task, between

# REPETICIÓN DEL CONCEPTO:
# En Locust, cada "Usuario Virtual" es una instancia de una clase que hereda de HttpUser.
# Piensa en esta clase como el plano o molde para fabricar clones de usuarios que atacarán la API.

class SimulacionUsuariosAlberto(HttpUser):
    
    # EJEMPLO SENCILLO:
    # wait_time simula el comportamiento humano. Un humano no hace clic 100 veces por segundo.
    # Aquí le decimos a cada clon que espere un tiempo aleatorio entre 1 y 3 segundos
    # antes de volver a lanzar otra petición al servidor.
    wait_time = between(1, 3)

    # El decorador @task le dice a Locust: "Esto es una acción que el usuario debe hacer"
    @task
    def probar_endpoint_get(self):
        # EJEMPLO: self.client funciona exactamente igual que el cliente de API de Playwright.
        # Le va a pegar al endpoint "/posts" usando el método GET.
        # No ponemos la URL completa porque se la inyectaremos desde la interfaz gráfica.
        self.client.get("/posts")

    @task
    def probar_endpoint_post(self):
        # EJEMPLO: También podemos estresar la creación de datos enviando un JSON ficticio.
        payload_falso = {
            "title": "Post de Carga",
            "body": "Probando rendimiento del servidor",
            "userId": 99
        }
        self.client.post("/posts", json=payload_falso)
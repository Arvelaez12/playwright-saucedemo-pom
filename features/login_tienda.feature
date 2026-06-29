# language: es
Característica: Control de acceso a la tienda virtual

  Escenario: Iniciar sesión de forma exitosa con credenciales válidas
    Dado que el usuario navega a la página de inicio de SauceDemo
    Cuando introduce el usuario "standard_user" en el formulario
    Y proporciona la contraseña "secret_sauce"
    Entonces el sistema debe permitirle el ingreso a la pantalla del catálogo
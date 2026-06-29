# language: es
Característica: Pruebas de Login Masivas con Tablas

  Esquema del escenario: Validar diferentes tipos de usuarios en SauceDemo
    Dado que el usuario abre la página de inicio de SauceDemo
    Cuando ingresa el texto "<usuario>" en el campo de username
    Y escribe la contraseña "<contraseña>" en el campo de password
    Y hace clic en el botón de Login
    Entonces el sistema debe validar el comportamiento esperado

    Ejemplos:
      | usuario         | contraseña     |
      | standard_user   | secret_sauce   |
      | locked_out_user | secret_sauce   |
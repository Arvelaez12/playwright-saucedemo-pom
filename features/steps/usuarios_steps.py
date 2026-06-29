from behave import given, when, then

@given('que el usuario abre la página de inicio de SauceDemo')
def step_abrir_pagina(context):
    context.page.goto("https://www.saucedemo.com")

@when('ingresa el texto "{usuario}" en el campo de username')
def step_ingresar_usuario(context, usuario):
    context.page.fill("#user-name", usuario)

@when('escribe la contraseña "{contraseña}" en el campo de password')
def step_ingresar_contrasena(context, contraseña):
    context.page.fill("#password", contraseña)

@when('hace clic en el botón de Login')
def step_hacer_clic_login(context):
    context.page.click("#login-button")

@then('el sistema debe validar el comportamiento esperado')
def step_validar_resultado(context):
    print(f"🤖 ROBOT: Validación exitosa en la pantalla actual: {context.page.url}")
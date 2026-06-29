from behave import given, when, then

# REPETICIÓN DEL CONCEPTO:
# Usamos un decorador @given con la frase EXACTA que escribimos en el archivo de texto.

@given('que el usuario navega a la página de inicio de SauceDemo')
def paso_abrir_navegador(context):
    # EJEMPLO DETALLADO:
    # Aquí adentro llamas a tu Page Object Model (POM) que ya construiste
    # Ejemplo: context.login_page.ir_a_la_url()
    print("🤖 ROBOT: Abriendo la página de SauceDemo...")
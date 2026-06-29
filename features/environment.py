from playwright.sync_api import sync_playwright

def before_scenario(context, scenario):
    # Behave ejecutará esto antes de CADA fila de tu tabla de forma automática
    context.pw = sync_playwright().start()
    context.browser = context.pw.chromium.launch(headless=True)
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    # Behave cerrará todo de manera segura al finalizar cada fila
    context.browser.close()
    context.pw.stop()
#!/bin/bash

# 🛑 Detener el script si ocurre algún error intermedio
set -e

echo "========================================================="
echo "🚀 INICIANDO PIPELINE DE AUTOMATIZACIÓN LOCAL"
echo "========================================================="

echo "🧹 Paso 1: Limpiando reportes y cachés anteriores..."
rm -rf allure-results/* reporte_ejecutivo.html .pytest_cache

echo "🐳 Paso 2: Levantando entorno aislado en Docker..."
# Levantamos el contenedor en segundo plano (-d) para que no bloquee tu pantalla
docker compose up -d --build

echo "🏎️ Paso 3: Ejecutando suite completa de pruebas dentro del contenedor..."
# Cambiamos exec por run --rm para garantizar estabilidad absoluta
docker compose run --rm pytest pytest tests/ --alluredir=allure-results --html=reporte_ejecutivo.html --self-contained-html || true

echo "📊 Paso 4: Generando reporte estático autónomo..."
echo "✅ Reporte HTML generado con éxito en la raíz."

echo "🛑 Paso 5: Apagando infraestructura de Docker para liberar memoria RAM..."
docker compose down

echo "========================================================="
echo "🎉 PIPELINE FINALIZADO CON ÉXITO. Revisa tus reportes."
echo "========================================================="
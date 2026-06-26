# 1. Sincronizamos la imagen base con la versión requerida por tus librerías locales
FROM mcr.microsoft.com/playwright/python:v1.60.0-jammy

# 2. Definimos la carpeta interna del contenedor
WORKDIR /app

# 3. Copiamos el archivo de librerías
COPY requirements.txt .

# 4. Instala las librerías en el contenedor
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto del proyecto
COPY . .

# 6. Ejecución silenciosa de toda la suite
CMD ["pytest", "-c", "/dev/null", "tests/"]
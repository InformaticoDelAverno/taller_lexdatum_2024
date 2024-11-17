# Usar una imagen base de Ubuntu
FROM ubuntu:20.04

# Establecer variables de entorno para evitar prompts de instalación
ENV DEBIAN_FRONTEND=noninteractive

# Actualizar el sistema e instalar dependencias
RUN apt-get update && \
    apt-get install -y python3 python3-pip git openjdk-11-jdk-headless unzip wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar las dependencias de Python
RUN pip install androguard

# Establecer directorio de trabajo para el script de análisis
WORKDIR /app

# Copiar el script de análisis de APK
COPY analizar_apk.py /app/

# Definir el comando de entrada para ejecutar el análisis
ENTRYPOINT ["python3", "/app/analizar_apk.py"]


#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <ruta_al_apk>"
    exit 1
fi

APK_PATH=$(realpath "$1")
APK_DIR=$(dirname "$APK_PATH")
APK_FILE=$(basename "$APK_PATH")

# Ejecutar el contenedor con el APK montado
docker run --rm -v "$APK_DIR:/apk" androguard-analyzer "/apk/$APK_FILE"

if [ $? -eq 0 ]; then
  echo "Análisis completado. Revisa el archivo de evidencias junto al APK."
else
  echo "Error durante el análisis del APK."
  exit 1
fi


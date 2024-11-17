#!/bin/bash

# Crear la imagen Docker
docker build -t androguard-analyzer .
if [ $? -eq 0 ]; then
  echo "Imagen Docker 'androguard-analyzer' creada con éxito."
else
  echo "Error al crear la imagen Docker."
  exit 1
fi


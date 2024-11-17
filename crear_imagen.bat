@echo off
echo Creando la imagen Docker 'androguard-analyzer'...
docker build -t androguard-analyzer .
if %errorlevel%==0 (
    echo Imagen Docker creada con exito.
) else (
    echo Error al crear la imagen Docker.
    exit /b 1
)


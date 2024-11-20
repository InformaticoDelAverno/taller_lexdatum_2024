@echo off
if "%~1"=="" (
    echo Uso: ejecutar_analisis.bat ^<ruta_al_apk^>
    exit /b 1
)

:: Guardar la ruta del APK y su directorio/nombre
set "APK_PATH=%~1"
for %%I in ("%APK_PATH%") do set "APK_DIR=%%~dpI"
for %%I in ("%APK_PATH%") do set "APK_FILE=%%~nxI"

:: Mostrar información de depuración (opcional)
echo APK_PATH: "%APK_PATH%"
echo APK_DIR: "%APK_DIR%"
echo APK_FILE: "%APK_FILE%"

echo Ejecutando análisis del APK...
docker run --rm -v "%APK_DIR%:/apk" androguard-analyzer "/apk/%APK_FILE%"

:: Verificar si el comando se ejecutó correctamente
if errorlevel 1 (
    echo Error durante el análisis del APK.
    exit /b 1
) else (
    echo Análisis completado. Revisa el archivo de evidencias junto al APK.
)


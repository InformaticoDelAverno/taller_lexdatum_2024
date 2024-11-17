@echo off
if "%~1"=="" (
    echo Uso: ejecutar_analisis.bat <ruta_al_apk>
    exit /b 1
)

set APK_PATH=%~1
for %%I in ("%APK_PATH%") do set APK_DIR=%%~dpI
for %%I in ("%APK_PATH%") do set APK_FILE=%%~nxI

echo Ejecutando análisis del APK...
docker run --rm -v "%APK_DIR%:/apk" androguard-analyzer "/apk/%APK_FILE%"

if %errorlevel%==0 (
    echo Análisis completado. Revisa el archivo de evidencias junto al APK.
) else (
    echo Error durante el análisis del APK.
    exit /b 1
)


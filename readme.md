# Análisis de APK con Docker y Androguard
Este proyecto proporciona un entorno Docker para analizar archivos APK y encontrar métodos relacionados con el impacto en la privacidad.

Los resultados se generan junto al APK analizado.

## Dependencias
### Requisitos generales
#### 1-Docker:
[Instalar Docker.](https://docs.docker.com/engine/install/)

#### 2-Acceso a un terminal o consola:

Linux/macOS: Bash terminal.

Windows: CMD o PowerShell.
### Scripts incluidos
#### Linux/macOS:
- crear_imagen.sh
- ejecutar_analisis.sh.

#### Windows:
- crear_imagen.bat
- ejecutar_analisis.bat.
## Instrucciones por sistema operativo
### Linux y macOS
#### Paso 1: Descargar el repositorio
[Descargar repositorio](https://codeload.github.com/InformaticoDelAverno/taller_lexdatum_2024/zip/refs/heads/main)
#### Paso 2: Construir la imagen Docker
Ejecuta el siguiente script para construir la imagen Docker:

```
./crear_imagen.sh
```
#### Paso 3: Ejecutar el análisis
```
./ejecutar_analisis.sh /ruta/a/tu/archivo.apk
```
Asegúrate de reemplazar /ruta/a/tu/archivo.apk con la ruta al archivo APK que deseas analizar.

Los resultados se guardarán junto al archivo APK, con un nombre como archivo_evidencias.txt.
### Windows
#### Paso 1: Descargar el repositorio
[Descargar repositorio](https://codeload.github.com/InformaticoDelAverno/taller_lexdatum_2024/zip/refs/heads/main)
#### Paso 2: Construir la imagen Docker
Ejecuta el script crear_imagen.bat:
```
crear_imagen.bat
```

#### Paso 3: Ejecutar el análisis
Para analizar un archivo APK:
```
ejecutar_analisis.bat "C:\ruta\a\tu\archivo.apk"
```
Reemplaza "C:\ruta\a\tu\archivo.apk" con la ruta al archivo APK que deseas analizar.

Los resultados se guardarán junto al archivo APK, con un nombre como archivo_evidencias.txt.

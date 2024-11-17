import sys
import logging
from androguard.misc import AnalyzeAPK
import os

for logger_name in logging.root.manager.loggerDict:
    logging.getLogger(logger_name).setLevel(logging.WARNING)
# Diccionario de métodos de impacto en la privacidad
privacy_impact_methods = [
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getDeviceId"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getImei"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getMeid"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getSimSerialNumber"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getSubscriberId"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getLine1Number"},
    {"class_name": "Landroid/os/Build;", "method_name": "getSerial"},
    {"class_name": "Landroid/provider/Settings$Secure;", "method_name": "getAndroidId"},
    {"class_name": "Landroid/accounts/Account;", "method_name": "getId"},
    {"class_name": "Landroid/os/UserManager;", "method_name": "getUserId"},
    {"class_name": "Landroid/location/LocationManager;", "method_name": "getLastKnownLocation"},
    {"class_name": "Landroid/location/LocationManager;", "method_name": "requestLocationUpdates"},
    {"class_name": "Landroid/location/Location;", "method_name": "getLatitude"},
    {"class_name": "Landroid/location/Location;", "method_name": "getLongitude"},
    {"class_name": "Landroid/location/Location;", "method_name": "getAltitude"},
    {"class_name": "Landroid/location/Location;", "method_name": "getSpeed"},
    {"class_name": "Landroid/location/Location;", "method_name": "getBearing"},
    {"class_name": "Landroid/location/Location;", "method_name": "getAccuracy"},
    {"class_name": "Landroid/hardware/SensorManager;", "method_name": "getSensorList"},
    {"class_name": "Landroid/hardware/SensorManager;", "method_name": "registerListener"},
    {"class_name": "Landroid/content/Context;", "method_name": "openFileOutput"},
    {"class_name": "Ljava/io/FileOutputStream;", "method_name": "write"},
    {"class_name": "Ljava/io/File;", "method_name": "createNewFile"},
    {"class_name": "Ljava/io/File;", "method_name": "mkdirs"},
    {"class_name": "Landroid/os/Environment;", "method_name": "getExternalStorageDirectory"},
    {"class_name": "Landroid/content/Context;", "method_name": "getExternalFilesDir"},
    {"class_name": "Landroid/content/Context;", "method_name": "getCacheDir"},
    {"class_name": "Landroid/content/Context;", "method_name": "openFileInput"},
    {"class_name": "Landroid/net/wifi/WifiInfo;", "method_name": "getMacAddress"},
    {"class_name": "Landroid/net/wifi/WifiInfo;", "method_name": "getSSID"},
    {"class_name": "Landroid/net/wifi/WifiInfo;", "method_name": "getBSSID"},
    {"class_name": "Landroid/net/wifi/WifiManager;", "method_name": "getScanResults"},
    {"class_name": "Landroid/net/wifi/WifiManager;", "method_name": "getConnectionInfo"},
    {"class_name": "Landroid/net/ConnectivityManager;", "method_name": "getActiveNetworkInfo"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getNetworkOperator"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getNetworkType"},
    {"class_name": "Landroid/telephony/TelephonyManager;", "method_name": "getCellLocation"},
    {"class_name": "Landroid/media/MediaRecorder;", "method_name": "startRecording"},
    {"class_name": "Landroid/media/MediaRecorder;", "method_name": "start"},
    {"class_name": "Landroid/hardware/camera2/CameraDevice;", "method_name": "takePicture"},
    {"class_name": "Landroid/hardware/camera2/CameraManager;", "method_name": "openCamera"},
    {"class_name": "Landroid/hardware/camera2/CameraManager;", "method_name": "getCameraIdList"},
    {"class_name": "Landroid/media/AudioManager;", "method_name": "getMicrophoneInfo"},
    {"class_name": "Landroid/accounts/AccountManager;", "method_name": "getAccounts"},
    {"class_name": "Landroid/accounts/AccountManager;", "method_name": "getAllAccounts"},
    {"class_name": "Landroid/accounts/AccountManager;", "method_name": "getUserData"},
    {"class_name": "Landroid/content/ClipboardManager;", "method_name": "getPrimaryClip"},
    {"class_name": "Landroid/content/ClipboardManager;", "method_name": "getSecondaryClip"},
    {"class_name": "Landroid/app/ActivityManager;", "method_name": "getRecentTasks"},
    {"class_name": "Landroid/app/ActivityManager;", "method_name": "getRunningTasks"},
    {"class_name": "Landroid/content/Context;", "method_name": "getSharedPreferences"},
    {"class_name": "Landroid/content/SharedPreferences;", "method_name": "edit"},
    {"class_name": "Landroid/content/SharedPreferences$Editor;", "method_name": "putString"},
    {"class_name": "Landroid/content/SharedPreferences$Editor;", "method_name": "putInt"},
    {"class_name": "Landroid/content/SharedPreferences$Editor;", "method_name": "apply"},
    {"class_name": "Landroid/content/ContentResolver;", "method_name": "insert"},
    {"class_name": "Landroid/content/ContentResolver;", "method_name": "update"},
    {"class_name": "Landroid/content/ContentResolver;", "method_name": "delete"},
    {"class_name": "Landroid/content/ContentResolver;", "method_name": "query"},
    {"class_name": "Landroid/database/sqlite/SQLiteDatabase;", "method_name": "execSQL"},
    {"class_name": "Landroid/content/Context;", "method_name": "getSystemService"},
    {"class_name": "Landroid/content/Context;", "method_name": "registerReceiver"},
    {"class_name": "Landroid/content/Context;", "method_name": "sendBroadcast"},
    {"class_name": "Landroid/content/ClipboardManager;", "method_name": "getClipboardText"},
    {"class_name": "Landroid/os/BatteryManager;", "method_name": "getBatteryCapacity"},
    {"class_name": "Landroid/os/PowerManager;", "method_name": "isDeviceIdleMode"},
    {"class_name": "Landroid/os/PowerManager;", "method_name": "isIgnoringBatteryOptimizations"},
    {"class_name": "Landroid/app/ApplicationPackageManager;", "method_name": "getInstalledApplications"},
    {"class_name": "Landroid/app/ApplicationPackageManager;", "method_name": "getInstalledPackages"},
    {"class_name": "Landroid/app/ApplicationPackageManager;", "method_name": "getPackageInfo"},
    {"class_name": "Landroid/bluetooth/BluetoothAdapter;", "method_name": "getBondedDevices"},
    {"class_name": "Landroid/bluetooth/BluetoothAdapter;", "method_name": "startDiscovery"},
    {"class_name": "Landroid/bluetooth/BluetoothDevice;", "method_name": "getName"},
    {"class_name": "Landroid/telephony/SmsManager;", "method_name": "sendTextMessage"},
    {"class_name": "Landroid/telephony/SmsManager;", "method_name": "sendMultipartTextMessage"},
    {"class_name": "Landroid/provider/ContactsContract$RawContacts$Data;", "method_name": "addEmail"},
    {"class_name": "Lcom/google/android/gms/location/ActivityRecognitionClient;", "method_name": "requestActivityUpdates"},
    {"class_name": "Landroidx/health/connect/client/HealthConnectClient;", "method_name": "registerDataType"},
    {"class_name": "Landroidx/health/connect/client/HealthConnectClient;", "method_name": "insertData"}
]



def find_method_usages(apk_path, search_parameters):
    try:
        # Cargar el APK y obtener los objetos DEX y de análisis
        a, d, dx = AnalyzeAPK(apk_path)
    except Exception as e:
        print(f"Error al analizar el APK: {e}")
        return

    print("Buscando métodos de impacto en la privacidad en el APK:")

    # Preparar un archivo para guardar los resultados
    result_file = os.path.splitext(apk_path)[0] + "_evidencias.txt"
    with open(result_file, "w", encoding="utf-8") as file:
        file.write("Evidencias encontradas durante el análisis del APK:\n\n")

        # Buscar usos de los métodos especificados en `search_parameters`
        for param in search_parameters:
            method_name = param['method_name']
            class_name = param['class_name']
            found = False

            # Recorrer cada clase en el archivo DEX
            for cls in d:
                for method in cls.get_methods():
                    code = method.get_code()
                    if code:  # Comprobar que el método tiene código asociado
                        bc = code.get_bc()
                        for i in bc.get_instructions():
                            if method_name in str(i) and class_name in str(i):
                                found = True
                                try:
                                    source = method.get_source()
                                except Exception:
                                    source = "Información no disponible"
                                
                                # Mostrar resultado en pantalla y guardar en el archivo
                                evidence = f"""
---- Evidencia encontrada ----
Clase buscada: {class_name}
Método buscado: {method_name}
Clase encontrada: {method.class_name}
Método encontrado: {method.get_name()}
Código fuente: {source}
Instrucción: {i}
-----------------------------
"""
                                print(evidence)
                                file.write(evidence)
            if not found:
                message = f"No se encontró el método {method_name} en la clase {class_name}.\n"
                print(message)
                file.write(message)
    os.chmod(result_file, 0o777)
    print(f"Resultados escritos en: {result_file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <ruta_del_apk>")
        sys.exit(1)

    apk_path = sys.argv[1]
    find_method_usages(apk_path, privacy_impact_methods)

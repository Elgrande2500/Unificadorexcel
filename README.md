## Script para Unión de Archivos Excel
Este proyecto contiene un script en Python diseñado para procesar y unir archivos de Excel utilizando la librería Pandas.
Para evitar conflictos con entornos gestionados por el sistema operativo (externally-managed-environment), fallos de certificados SSL o errores de módulos faltantes en el Python global (como _ctypes), la ejecución se gestiona de forma aislada y automática mediante uv.
## 🚀 Requisitos e Instalación
No es necesario configurar entornos virtuales (venv) ni usar pip manualmente. Sigue estos pasos para preparar tu entorno:
## 1. Instalar uv (Gestor de entornos y paquetes)
Abre tu terminal y ejecuta el instalador oficial para Linux y macOS:

# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

Nota: Una vez finalizada la instalación, cierra la terminal actual y abre una nueva pestaña (o ejecuta source ~/.bashrc) para que el sistema reconozca el comando uv.

## 2. Instalar dependencias del sistema (Interfaz Gráfica)
Si tu script utiliza ventanas emergentes o interfaces gráficas a través de tkinter, asegúrate de tener el paquete del sistema instalado:

sudo apt update && sudo apt install python3-tk -y

------------------------------
## 💻 Ejecución del Script
Para ejecutar el script de forma segura, ordenamos a uv que descargue una versión estable y limpia de Python (ignoring versiones del sistema que puedan estar incompletas) e inyecte las librerías necesarias al vuelo:

   1. Desplázate a la carpeta del proyecto:
   
   cd "/home/angel/Escritorio/Script para union"
   
   2. Ejecuta el siguiente comando:
   
   uv run --python 3.12 --with pandas --with openpyxl python3 scriptexcel.py
   
   
## ¿Qué hace este comando?

* --python 3.12: Descarga y utiliza una versión de Python oficial, aislando la ejecución de cualquier versión corrupta del sistema.
* --with pandas --with openpyxl: Instala temporalmente las librerías necesarias para leer y escribir archivos de Excel de forma rápida y segura.

------------------------------
## 🛠️ Solución de Problemas Comunes

* Error ModuleNotFoundError: No module named '_ctypes' o fallos SSL: Ocurre si olvidas incluir el parámetro --python 3.12. Asegúrate de usar el comando de ejecución completo detallado arriba.
* Comando uv no encontrado: Recuerda reiniciar tu terminal o abrir una nueva ventana después de instalar uv.

------------------------------
¿Te gustaría agregar alguna sección extra al README? Por ejemplo, podemos detallar qué hace exactamente el script con los archivos de Excel o dónde debe colocar el usuario los archivos de entrada.

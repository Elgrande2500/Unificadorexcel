import pandas as pd
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox

def seleccionar_archivos():
    root = tk.Tk()
    root.withdraw()
    archivos = filedialog.askopenfilenames(
        title="Selecciona los archivos Excel",
        filetypes=[("Archivos Excel", "*.xlsx *.xls")]
    )
    return archivos

def pedir_columnas():
    root = tk.Tk()
    root.withdraw()
    columnas = simpledialog.askstring(
        "Columnas",
        "Ingresa los nombres de las columnas separados por coma:\nEjemplo: Nombre, Edad, Precio"
    )
    if columnas:
        return [col.strip() for col in columnas.split(",")]
    return []

def procesar_archivos(archivos, columnas_deseadas):
    dataframes = []

    for archivo in archivos:
        try:
            df = pd.read_excel(archivo)

            # Validar columnas existentes
            columnas_existentes = [col for col in columnas_deseadas if col in df.columns]

            if not columnas_existentes:
                print(f"⚠️ Ninguna columna válida en: {archivo}")
                continue

            df_filtrado = df[columnas_existentes]
            df_filtrado["Archivo_Origen"] = archivo  # opcional
            dataframes.append(df_filtrado)

        except Exception as e:
            print(f"❌ Error en {archivo}: {e}")

    if dataframes:
        return pd.concat(dataframes, ignore_index=True)
    else:
        return None

def guardar_excel(df_final):
    root = tk.Tk()
    root.withdraw()
    ruta_guardado = filedialog.asksaveasfilename(
        defaultextension=".xlsx",
        filetypes=[("Archivo Excel", "*.xlsx")],
        title="Guardar archivo final"
    )

    if ruta_guardado:
        df_final.to_excel(ruta_guardado, index=False)
        messagebox.showinfo("Éxito", f"Archivo guardado en:\n{ruta_guardado}")

def main():
    archivos = seleccionar_archivos()
    if not archivos:
        print("No se seleccionaron archivos.")
        return

    columnas = pedir_columnas()
    if not columnas:
        print("No se especificaron columnas.")
        return

    df_final = procesar_archivos(archivos, columnas)

    if df_final is not None:
        guardar_excel(df_final)
    else:
        print("No se generó ningún archivo.")

if __name__ == "__main__":
    main()
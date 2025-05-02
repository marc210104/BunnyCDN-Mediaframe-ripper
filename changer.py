import re
import subprocess
import os
import sys

BASE_DIR = r"C:\\Users\\marco\\Videos\\Bunny CDN"

OPCIONES = {
    "EDOS": [],
    "F3": [
        "Parcial",
        "Intensivo Parcial",
        "Post Parcial",
        "Intensivo Final"
    ],
    "Mecanica": [],
    "Circuits": [
        "Post Parcial",
        "Intensivo Final"
    ],
}

def seleccionar_carpeta():
    print("\nAsignaturas disponibles:")
    claves = list(OPCIONES.keys())
    for i, carpeta in enumerate(claves):
        print(f"  [{i+1}] {carpeta}")
    seleccion = int(input("Selecciona la asignatura (número): ")) - 1

    if seleccion < 0 or seleccion >= len(claves):
        print("Selección inválida.")
        sys.exit(1)

    asignatura = claves[seleccion]
    subcarpetas = OPCIONES[asignatura]

    if subcarpetas:
        print(f"\nSubcarpetas dentro de {asignatura}:")
        for j, sub in enumerate(subcarpetas):
            print(f"  [{j+1}] {sub}")
        sub_sel = int(input("Selecciona la subcarpeta (número): ")) - 1

        if sub_sel < 0 or sub_sel >= len(subcarpetas):
            print("Selección inválida.")
            sys.exit(1)

        return os.path.join(BASE_DIR, asignatura, subcarpetas[sub_sel])
    else:
        return os.path.join(BASE_DIR, asignatura)

def modificar_script(ruta_script):
    url = input("Introduce la URL completa del embed (iframe): ").strip()
    nombre = input("Introduce el nuevo nombre para el archivo (sin extensión): ").strip()

    carpeta_destino = seleccionar_carpeta()
    os.makedirs(carpeta_destino, exist_ok=True)

    with open(ruta_script, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    lineas[177] = f'        referer="{url}",\n'
    lineas[179] = f'        embed_url="{url}",\n'
    lineas[181] = f'        name="{nombre}",\n'
    lineas[183] = f'        path=r"{carpeta_destino}",\n'

    print("\nCambios realizados:")
    print(f"Nuevo referer/embed_url: {url}")
    print(f"Nuevo nombre: {nombre}.mp4")
    print(f"Ruta de guardado: {carpeta_destino}")

    with open(ruta_script, "w", encoding="utf-8") as archivo:
        archivo.writelines(lineas)

    print("\nArchivo actualizado correctamente.")

    subprocess.run([
        sys.executable, ruta_script
    ], cwd=os.path.dirname(ruta_script))

if __name__ == "__main__":
    ruta_script = r"C:\\Users\\marco\\Videos\\Bunny CDN\\drm-ases.py"
    modificar_script(ruta_script)

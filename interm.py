import subprocess

# Directorio específico del script
ruta_directorio = r"C:\Users\marco\Videos\Bunny CDN\Prueba"

# Comando para ejecutar en PowerShell
comando = f'cd "{ruta_directorio}"; python drm-ases.py'

# Ejecutar el comando en una nueva ventana de PowerShell
subprocess.run(["powershell", "-NoExit", "-Command", comando])
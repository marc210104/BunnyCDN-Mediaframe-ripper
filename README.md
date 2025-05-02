# BunnyCDN-Mediaframe-ripper
This set of scripts enables the automated download of DRM-protected videos hosted on Bunny CDN by simulating embed access and using `yt_dlp` to retrieve the video.

ENGLISH
-------

Description:
This set of scripts enables the automated download of DRM-protected videos hosted on Bunny CDN by simulating embed access and using `yt_dlp` to retrieve the video.

Components:
- drm-ases.py  → Main script to simulate DRM pings and download the video.
- changer.py   → Interactive helper that injects URL, filename, and path into `drm-ases.py`.
- interm.py    → Launches `drm-ases.py` from a specific directory via PowerShell.
- MERLIN.bat   → Optional batch launcher (purpose to be confirmed).

Usage:
1. Run `changer.py`:
   - Paste the embed iframe URL.
   - Enter the desired filename (without extension).
   - Choose a subject and subfolder.
   - It will automatically modify `drm-ases.py` and launch the download.

Requirements:
- Python 3.x
- Installed modules: `requests`, `yt_dlp`
- Valid access to the Bunny CDN embed

ESPAÑOL
-------

Descripción:
Este conjunto de scripts permite descargar vídeos protegidos de Bunny CDN utilizando una URL de tipo iframe embed.
Está diseñado para automatizar el cambio de parámetros (URL, nombre, ruta) y lanzar la descarga con `yt_dlp`.

Componentes:
- drm-ases.py  → Script principal que simula tráfico DRM y descarga el vídeo.
- changer.py   → Script interactivo que modifica `drm-ases.py` con nueva URL, nombre y destino.
- interm.py    → Lanza `drm-ases.py` desde una carpeta específica con PowerShell.
- MERLIN.bat   → Posible lanzador de automatización (por revisar contenido exacto).

Uso:
1. Ejecuta `changer.py`:
   - Introduce el iframe embed.
   - Especifica el nombre del vídeo (sin extensión).
   - Selecciona la asignatura y carpeta donde guardar.
   - Se modificará automáticamente `drm-ases.py` con esos datos.
   - El script lanza `drm-ases.py` para realizar la descarga.

Requisitos:
- Python 3.x
- Módulos instalados: `requests`, `yt_dlp`
- Acceso válido al iframe de Bunny CDN

Notas:
- La estructura de carpetas está basada en asignaturas.
- El script se adapta fácilmente a nuevas asignaturas añadiéndolas al diccionario `OPCIONES` en `changer.py`.
- El archivo descargado es `.mp4` y se guarda en la ruta seleccionada.

-------------------------------
Notes:
- Folder structure is based on academic subjects.
- Add new subjects or folders in `changer.py` under the `OPCIONES` dictionary.
- The video is saved as `.mp4` in the selected location.

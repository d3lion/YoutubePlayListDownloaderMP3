import os
import shutil
from yt_dlp import YoutubeDL

def verificar_ffmpeg():
    """Verifica si ffmpeg está instalado en el sistema."""
    if shutil.which("ffmpeg") is None:
        print("⚠️ No se encontró ffmpeg. Por favor, instálalo para convertir a MP3 correctamente.")
        exit(1)

def descargar_audio(url, nombre_carpeta):
    """Descarga un solo audio en formato MP3."""
    os.makedirs(nombre_carpeta, exist_ok=True)
    opciones = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(nombre_carpeta, '%(title)s.%(ext)s'),
    }
    try:
        with YoutubeDL(opciones) as ydl:
            print("\n⬇️ Descargando audio, por favor espera...")
            ydl.download([url])
        print(f"\n✅ ¡Descarga completada! El archivo MP3 está en la carpeta '{nombre_carpeta}'.")
    except Exception as e:
        print(f"❌ Error durante la descarga: {str(e)}")

def descargar_playlist():
    """Descarga una playlist de YouTube en formato MP3."""
    verificar_ffmpeg()
    url = input("Introduce la URL de la playlist de YouTube: ").strip()
    
    if not url.startswith(("http://", "https://")):
        print("❌ URL no válida. Introduce una URL correcta.")
        return
    
    nombre_carpeta = input("¿Cómo quieres llamar a la carpeta donde se guardarán los MP3? ").strip()
    os.makedirs(nombre_carpeta, exist_ok=True)
    
    opciones_info = {
        'quiet': True,
        'extract_flat': True,
    }
    
    try:
        with YoutubeDL(opciones_info) as ydl:
            resultado = ydl.extract_info(url, download=False)
            if not resultado or "entries" not in resultado:
                print("❌ No se pudo obtener información de la playlist.")
                return
            
            videos = resultado['entries']
            total_videos = len(videos)
            print("\n📜 Videos en la playlist:")
            for i, video in enumerate(videos, 1):
                print(f"{i}. {video.get('title', 'Sin título')}")
            
            while True:
                try:
                    inicio = int(input(f"\n¿Desde qué número de canción quieres empezar (1-{total_videos})? ")) - 1
                    if 0 <= inicio < total_videos:
                        break
                    print(f"⚠️ Ingresa un número entre 1 y {total_videos}.")
                except ValueError:
                    print("⚠️ Ingresa un número válido.")
    
    except Exception as e:
        print(f"❌ Error al obtener la información de la playlist: {str(e)}")
        return
    
    opciones_descarga = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(nombre_carpeta, '%(title)s.%(ext)s'),
        'noplaylist': False,
        'playliststart': inicio + 1,
    }
    
    try:
        print(f"\n⬇️ Descargando la playlist desde la canción {inicio + 1}, por favor espera...")
        with YoutubeDL(opciones_descarga) as ydl:
            ydl.download([url])
        print(f"\n✅ ¡Descarga completada! Los archivos MP3 están en la carpeta '{nombre_carpeta}'.")
    except Exception as e:
        print(f"❌ Ocurrió un error durante la descarga: {str(e)}")

def main():
    verificar_ffmpeg()
    print("\n🎵 Bienvenido al descargador de YouTube 🎵")
    print("1. Descargar un solo MP3")
    print("2. Descargar una playlist completa")
    
    while True:
        opcion = input("\nElige una opción (1 o 2): ").strip()
        if opcion in ('1', '2'):
            break
        print("⚠️ Opción no válida. Ingresa 1 o 2.")
    
    url = input("Introduce la URL de YouTube: ").strip()
    nombre_carpeta = input("¿Cómo quieres llamar a la carpeta donde se guardará(n) el/los MP3? ").strip()
    
    if opcion == '1':
        descargar_audio(url, nombre_carpeta)
    else:
        descargar_playlist()

if __name__ == "__main__":
    main()

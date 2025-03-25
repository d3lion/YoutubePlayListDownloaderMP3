# 🎵 YoutubePlayListDownload

## 📄 Descripción

`YoutubePlayListDownload` es una herramienta en Python que permite descargar listas de reproducción completas o videos individuales de YouTube en formato MP3. Utiliza la librería `yt_dlp` para gestionar las descargas y `ffmpeg` para la conversión de formatos.

## 🌟 Características

- 📺 Descarga videos individuales de YouTube en formato MP3.
- 📜 Descarga listas de reproducción completas de YouTube en formato MP3.
- 🗂️ Guarda los archivos en una carpeta específica definida por el usuario.
- 🔍 Permite seleccionar desde qué número de canción empezar la descarga en una playlist.
- ⚙️ Interfaz de línea de comandos fácil de usar con opciones interactivas.

## 🛠️ Requisitos

- 🐍 Python 3.7 o superior.
- `yt-dlp` librería de Python para la descarga de videos de YouTube.
- `ffmpeg` para la conversión de audio.

## 📦 Instalación

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/d3lion/YoutubePlayListDownload.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd YoutubePlayListDownload
   ```

3. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

4. Asegúrate de tener `ffmpeg` instalado en tu sistema. Puedes descargarlo desde [aquí](https://ffmpeg.org/download.html).

## 🚀 Uso

Para usar `YoutubePlayListDownload`, simplemente ejecuta el script principal y sigue las instrucciones interactivas:

```bash
python main.py
```

### ⚙️ Opciones

- `1. Descargar un solo MP3`: Permite descargar un solo video de YouTube en formato MP3.
- `2. Descargar una playlist completa`: Permite descargar todos los videos de una lista de reproducción de YouTube en formato MP3.

### Ejemplo de Uso

1. Ejecuta el script principal:
   ```bash
   python main.py
   ```

2. Selecciona la opción deseada (`1` o `2`).
3. Introduce la URL de YouTube.
4. Especifica el nombre de la carpeta donde se guardarán los archivos MP3.
5. Si seleccionas la opción `2`, introduce el número desde el cual deseas comenzar la descarga.

## Contribución

¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos para contribuir:

1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-feature`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva feature'`).
4. Sube a tu fork (`git push origin feature/nueva-feature`).
5. Crea un nuevo Pull Request.

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 📧 Contacto

Para cualquier consulta o sugerencia, por favor contacta a d3lion@example.com.

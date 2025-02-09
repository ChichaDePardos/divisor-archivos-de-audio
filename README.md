# 🎵 Cortador de Audio para Windows

Herramienta intuitiva para dividir archivos WAV grandes en fragmentos manejables. ¡Con interfaz gráfica y barra de progreso!

## 🌟 Características Principales
- **Selector de archivos integrado** con inicio en Documentos
- **Barra de progreso visual** con porcentaje de avance
- **Mensajes con emojis** para mejor experiencia de usuario
- **Auto-detector de errores** con alertas claras
- **Salida en misma carpeta** del archivo original

## 📦 Requisitos Mínimos
- Windows 10/11 (64 bits)
- Python 3.8+ instalado
- [FFmpeg para Windows](https://ffmpeg.org/download.html#build-windows)

## 🚀 Instalación Rápida

1. **Instalar dependencias** (ejecutar en PowerShell):
```powershell
pip install pydub tqdm
```
2. **Descargar FFmpeg**:
```powershell
# Con Chocolatey (admin):
choco install ffmpeg

# Manualmente:
# 1. Descargar de https://www.gyan.dev/ffmpeg/builds/
# 2. Agregar a PATH: Panel de control → Sistema → Configuración avanzada
```

3. **Guardar el script** como `cortar_audio.py`

## 🖱️ Modo de Uso

1. **Hacer doble clic** en `cortar_audio.py`
2. Seleccionar archivo WAV en el explorador
3. Esperar a que termine la división
4. **¡Listo!** Los fragmentos estarán en la misma carpeta

**Ejemplo de salida**:
```
MiAudio_original.wav → 
├── MiAudio_parte1.wav
├── MiAudio_parte2.wav
└── MiAudio_parte3.wav
```

## ⚙️ Personalización Avanzada

### Cambiar tamaño máximo por fragmento
Editar línea 19 del script:
```python
def dividir_wav(archivo_entrada, tamano_max_mb=300):  # Cambiar 300 a tamaño deseado (MB)
```

### Modificar formato de salida
Cambiar línea 52:
```python
fragmento.export(nombre_salida, format="mp3")  # Cambiar "wav" a mp3, ogg, etc.
```

## 🚨 Solución de Problemas

**Error: "FileNotFoundError"**
- Verificar que FFmpeg esté instalado y en PATH
- Ejecutar PowerShell como administrador:
```powershell
[System.Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\ruta\a\ffmpeg\bin", "Machine")
```

**El progreso se congela**
- Desactivar antivirus temporalmente
- Usar rutas cortas sin espacios: `C:\Audios\mi_audio.wav`

**Calidad de audio baja**
- Asegurarse que el archivo original sea WAV sin compresión
- Aumentar el tamaño máximo por fragmento

## 📌 Ejemplo Práctico

**Caso**: Dividir grabación de 2 horas (1.2 GB) para email
```python
tamano_max_mb=25  # Límite común para adjuntos
```
**Resultado**:
- 48 fragmentos de ≈25 MB cada uno
- Duración por parte: ~2.5 minutos

## 📄 Licencia
Este proyecto usa licencia MIT. Ver [LICENSE](LICENSE) para detalles.

---

[Repositorio GitHub](https://github.com/ChichaDePardos/descarga-gaceta-indecopi) | [Documentación FFmpeg](https://ffmpeg.org/documentation.html)

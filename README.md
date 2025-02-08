# ✂️ Divisor de Archivos de Audio

Herramienta para dividir archivos WAV grandes en fragmentos manejables. Ideal para preparar material de audio que excede límites de tamaño en plataformas.


## 🌟 Para Todos los Públicos

**¿Para qué sirve?**  
Transforma archivos de audio gigantes en varios trozos más pequeños automáticamente. Perfecto si necesitas:
- Subir podcasts a plataformas con límites de tamaño
- Preparar muestras de audio para análisis
- Dividir grabaciones largas en capítulos

## 🧩 Requisitos Básicos
- **Tu archivo de audio**: Cualquier archivo .WAV (Ej: `grabacion_concert.wav`)
- **Espacio en disco**: 2x el tamaño del archivo original
- **Sistema**: Windows/macOS/Linux

## 🚀 Cómo Usarlo en 3 Pasos

1. **Prepara tu audio**  
   - Asegúrate que sea formato .WAV
   - Guárdalo en una carpeta fácil de acceder (Ej: `Escritorio/Audios`)

2. **Configura el script**  
   Abre `cortar-audio.py` y cambia esta línea:  
   ```python
   archivo_wav = "TU_RUTA_COMPLETA.wav"  # Ej: "C:/Usuarios/MiUsuario/Escritorio/grabacion.wav"
   ```

3. **Ejecuta el programa**  
   En tu terminal:  
   ```bash
   python cortar-audio.py
   ```

**Resultado Final**:  
Obtendrás varios archivos como `grabacion_parte1.wav`, `grabacion_parte2.wav`, etc.

---

## 🛠️ Versión para Técnicos

### 📋 Dependencias
```bash
pip install pydub tqdm
```
**Requisito adicional**:  
Instalar [FFmpeg](https://ffmpeg.org/) y agregarlo al PATH del sistema.

### ⚙️ Funcionamiento Interno
```python
# Lógica clave de división
duracion_fragmento_ms = math.floor(duracion_total_ms * (tamano_max_bytes / tamano_total))
```

**Parámetros Configurables**:
- Tamaño máximo por fragmento (MB):  
  ```python
  tamano_max_mb=300  # Valor por defecto - modificar según necesidad
  ```
- Formato de salida:  
  Cambiar `format="wav"` por otros soportados (mp3, ogg, etc.)

### 📊 Proceso Detallado
1. Calcula relación tamaño/duración del audio original
2. Divide en segmentos proporcionales al límite de tamaño
3. Exporta cada fragmento conservando calidad original
4. Muestra progreso con barra interactiva

### 🚨 Solución de Problemas Comunes

**Error: "File not found"**  
- Verificar rutas absolutas:  
  ```python
  "C:\\Carpeta\\Subcarpeta\\archivo.wav"  # Windows
  "/home/usuario/audios/archivo.wav"      # Linux/macOS
  ```

**Error de codec**  
Instalar FFmpeg y reiniciar consola:  
```bash
# Ubuntu/Debian
sudo apt install ffmpeg

# Windows (usando Chocolatey)
choco install ffmpeg
```

**Fragmentos de tamaño desigual**  
- Los últimos fragmentos pueden ser más pequeños por ajuste de división
- Para igualar duraciones, usar:  
  ```python
  duracion_fragmento_ms = 600000  # 10 minutos exactos (600,000 ms)
  ```

---

## 📌 Ejemplo Práctico

**Archivo Original**:  
- `entrevista.wav` (850 MB, 45 minutos)

**Ejecución**:  
```bash
python cortar-audio.py
```

**Resultado**:  
3 archivos:  
1. `entrevista_parte1.wav` (300 MB, 16 min)
2. `entrevista_parte2.wav` (300 MB, 16 min)  
3. `entrevista_parte3.wav` (250 MB, 13 min)

---

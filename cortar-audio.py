from pydub import AudioSegment
import os
import math
from tqdm import tqdm
from tkinter import Tk, filedialog
import sys

print(f"🎵 Selecciona el archivo de audio a convertir")
def seleccionar_archivo():
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo WAV a dividir",
        filetypes=[("Archivos WAV", "*.wav")],
        initialdir=os.path.expanduser("~\\Documents")  # Abre en Documentos por defecto
    )
    
    root.destroy()
    return archivo.replace("/", "\\")  # Normalizar rutas para Windows

def dividir_wav(archivo_entrada, tamano_max_mb=300):
    try:
        # Convertir tamaño máximo a bytes
        tamano_max_bytes = tamano_max_mb * 1024 * 1024

        # Cargar el archivo WAV
        audio = AudioSegment.from_wav(archivo_entrada)
        
        # Obtener ruta del directorio y nombre base
        directorio = os.path.dirname(archivo_entrada)
        nombre_base = os.path.splitext(os.path.basename(archivo_entrada))[0]
        
        # Obtener tamaño total del archivo y duración
        tamano_total = os.path.getsize(archivo_entrada)
        duracion_total_ms = len(audio)

        # Calcular duración de cada fragmento
        duracion_fragmento_ms = math.floor(duracion_total_ms * (tamano_max_bytes / tamano_total))

        # Dividir el archivo en partes
        parte = 1
        inicio = 0

        # Barra de progreso
        total_partes = math.ceil(duracion_total_ms / duracion_fragmento_ms)
        with tqdm(total=total_partes, desc="Dividiendo audio", unit="parte", bar_format="{l_bar}{bar:50}{r_bar}") as pbar:
            while inicio < duracion_total_ms:
                fin = inicio + duracion_fragmento_ms
                if fin > duracion_total_ms:
                    fin = duracion_total_ms
                
                fragmento = audio[inicio:fin]
                nombre_salida = os.path.join(directorio, f"{nombre_base}_parte{parte}.wav")
                fragmento.export(nombre_salida, format="wav")

                porcentaje = (parte / total_partes) * 100
                pbar.set_postfix_str(f"Parte {parte} [{porcentaje:.1f}%]")
                
                inicio = fin
                parte += 1
                pbar.update(1)

        print("\n✅ División completada exitosamente!")
        print(f"📁 Archivos guardados en: {directorio}")
        input("\nPresiona Enter para salir...")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        archivo = seleccionar_archivo()
        
        if not archivo:
            print("\n⚠️  No se seleccionó ningún archivo.")
            sys.exit()
            
        if not archivo.lower().endswith('.wav'):
            print("\n❌ Error: El archivo debe ser formato WAV (.wav)")
            sys.exit(1)
            
        print(f"\n🎵 Archivo seleccionado: {archivo}")
        dividir_wav(archivo)
        
    except KeyboardInterrupt:
        print("\n🛑 Proceso cancelado por el usuario")
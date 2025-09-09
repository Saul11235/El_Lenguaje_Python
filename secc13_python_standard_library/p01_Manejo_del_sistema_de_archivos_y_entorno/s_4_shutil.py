
import shutil
from pathlib import Path

# Crear directorios y archivos de ejemplo
origen = Path("carpeta_origen")
origen.mkdir(exist_ok=True)
(origen / "archivo.txt").write_text("Contenido de prueba.")

# 1. Copiar un archivo a otro lugar
shutil.copy("carpeta_origen/archivo.txt", "archivo_copiado.txt")
print("Archivo copiado a 'archivo_copiado.txt'.")

# 2. Copiar un archivo con permisos y metadata (más completo)
shutil.copy2("carpeta_origen/archivo.txt", "archivo_copiado_con_metadata.txt")
print("Archivo copiado con metadata.")

# 3. Copiar una carpeta completa (de forma recursiva)
destino = "copia_completa"
if not Path(destino).exists():
    shutil.copytree("carpeta_origen", destino)
    print("Carpeta completa copiada a 'copia_completa'.")

# 4. Mover un archivo o carpeta
shutil.move("archivo_copiado.txt", "archivo_movido.txt")
print("Archivo movido a 'archivo_movido.txt'.")

# 5. Eliminar una carpeta y todo su contenido
if Path("copia_completa").exists():
    shutil.rmtree("copia_completa")
    print("Carpeta 'copia_completa' eliminada.")

# 6. Comprimir una carpeta (zip)
shutil.make_archive("mi_archivo_zip", "zip", "carpeta_origen")
print("Carpeta comprimida en 'mi_archivo_zip.zip'.")

# 7. Extraer un archivo comprimido (zip)
shutil.unpack_archive("mi_archivo_zip.zip", "carpeta_extraida", "zip")
print("Archivo 'mi_archivo_zip.zip' extraído en 'carpeta_extraida'.")

print("Fin del script shutil.")

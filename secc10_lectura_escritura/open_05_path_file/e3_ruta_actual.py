# obteniendo la ruta de la carpeta
# del modulo actual

from pathlib import Path

print(Path(__file__).resolve().parent)


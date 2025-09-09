
import argparse

# Crear el parser
parser = argparse.ArgumentParser(description="Ejemplo simple con argparse")

# Definir argumentos
parser.add_argument("nombre", type=str, help="Tu nombre")
parser.add_argument("-e", "--edad", type=int, help="Tu edad", default=18)
parser.add_argument("-v", "--verbose", action="store_true", help="Modo detallado")

# Parsear los argumentos
args = parser.parse_args()

# Usar los argumentos
if args.verbose:
    print(f"Hola {args.nombre}, tienes {args.edad} años. ¡Modo detallado activado!")
else:
    print(f"Hola {args.nombre}!")


# python script.py Ana -e 25 -v

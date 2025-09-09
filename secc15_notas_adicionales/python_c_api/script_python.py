import ctypes

# Carga la librería compartida
lib = ctypes.CDLL('./milib.dll')

# Define el tipo de argumentos y retorno de la función C
lib.suma.argtypes = [ctypes.c_int, ctypes.c_int]
lib.suma.restype = ctypes.c_int

# Llama la función desde Python
resultado = lib.suma(3, 4)
print("Resultado:", resultado)  # Resultado: 7

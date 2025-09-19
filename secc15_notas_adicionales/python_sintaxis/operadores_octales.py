
# Definimos los números en octal
a = 0o15  # 13 en decimal (15 en octal)
b = 0o11  # 9 en decimal (11 en octal)

# Operaciones bit a bit
and_result = a & b        # AND a nivel de bits
or_result = a | b         # OR a nivel de bits
xor_result = a ^ b        # XOR a nivel de bits
not_result = ~a           # NOT a nivel de bits
shift_left_result = a << 2  # Desplazamiento a la izquierda
shift_right_result = a >> 2  # Desplazamiento a la derecha

# Imprimir los resultados en formato octal
print(f"a (octal): {oct(a)}")
print(f"b (octal): {oct(b)}")

# Mostrar resultados
print(f"AND: {oct(and_result)}")            # AND a nivel de bits
print(f"OR: {oct(or_result)}")              # OR a nivel de bits
print(f"XOR: {oct(xor_result)}")            # XOR a nivel de bits
print(f"NOT (a): {oct(not_result)}")        # NOT a nivel de bits
print(f"Desplazamiento a la izquierda: {oct(shift_left_result)}")  # Desplazamiento a la izquierda
print(f"Desplazamiento a la derecha: {oct(shift_right_result)}")  # Desplazamiento a la derecha

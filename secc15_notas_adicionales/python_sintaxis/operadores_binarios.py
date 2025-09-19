
# Definimos los números en binario
a = 0b1101  # 13 en binario
b = 0b1011  # 11 en binario

# Operaciones bit a bit
and_result = a & b        # AND a nivel de bits
or_result = a | b         # OR a nivel de bits
xor_result = a ^ b        # XOR a nivel de bits
not_result = ~a           # NOT a nivel de bits
shift_left_result = a << 2  # Desplazamiento a la izquierda
shift_right_result = a >> 2  # Desplazamiento a la derecha

# Imprimir los resultados en formato binario
print(f"a (binario): {bin(a)}")
print(f"b (binario): {bin(b)}")

# Mostrar resultados
print(f"AND: {bin(and_result)}")            # AND a nivel de bits
print(f"OR: {bin(or_result)}")              # OR a nivel de bits
print(f"XOR: {bin(xor_result)}")            # XOR a nivel de bits
print(f"NOT (a): {bin(not_result)}")        # NOT a nivel de bits
print(f"Desplazamiento a la izquierda: {bin(shift_left_result)}")  # Desplazamiento a la izquierda
print(f"Desplazamiento a la derecha: {bin(shift_right_result)}")  # Desplazamiento a la derecha

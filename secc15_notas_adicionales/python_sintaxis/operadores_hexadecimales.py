
# Definimos los números en hexadecimal
a = 0xA3  # 163 en decimal (A3 en hexadecimal)
b = 0x57  # 87 en decimal (57 en hexadecimal)

# Operaciones bit a bit
and_result = a & b        # AND a nivel de bits
or_result = a | b         # OR a nivel de bits
xor_result = a ^ b        # XOR a nivel de bits
not_result = ~a           # NOT a nivel de bits
shift_left_result = a << 2  # Desplazamiento a la izquierda
shift_right_result = a >> 2  # Desplazamiento a la derecha

# Imprimir los resultados en formato hexadecimal
print(f"a (hexadecimal): {hex(a)}")
print(f"b (hexadecimal): {hex(b)}")

# Mostrar resultados
print(f"AND: {hex(and_result)}")            # AND a nivel de bits
print(f"OR: {hex(or_result)}")              # OR a nivel de bits
print(f"XOR: {hex(xor_result)}")            # XOR a nivel de bits
print(f"NOT (a): {hex(not_result)}")        # NOT a nivel de bits
print(f"Desplazamiento a la izquierda: {hex(shift_left_result)}")  # Desplazamiento a la izquierda
print(f"Desplazamiento a la derecha: {hex(shift_right_result)}")  # Desplazamiento a la derecha

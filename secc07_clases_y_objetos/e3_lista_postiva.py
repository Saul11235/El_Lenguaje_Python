#
# LISTA POSITIVA
#
# Cree una clase heredada de list que sólo 
# admita números positivos al usar el método append.
#
# Nota: use la build-in function super() para acceder a la super clase
#

# -------------------------------------------------------

class ListaPositiva(list):
    def append(self, valor):
        if self._es_valido(valor):
            super().append(valor)
        else:
            print("ERROR: Solo se pueden añadir números positivos.")

    def extend(self, iterable):
        if all(self._es_valido(valor) for valor in iterable):
            super().extend(iterable)
        else:
            print("ERROR: Todos los elementos deben ser números positivos.")

    def insert(self, index, valor):
        if self._es_valido(valor):
            super().insert(index, valor)
        else:
            print("ERROR: Solo se pueden insertar números positivos.")

    def __setitem__(self, index, valor):
        # Permite asignación directa, como lista[0] = valor
        if isinstance(index, slice):
            if all(self._es_valido(v) for v in valor):
                super().__setitem__(index, valor)
            else:
                print("ERROR: Todos los elementos deben ser positivos.")
        else:
            if self._es_valido(valor):
                super().__setitem__(index, valor)
            else:
                print("ERROR: Solo se pueden asignar números positivos.")

    @staticmethod
    def _es_valido(valor):
        return isinstance(valor, (int, float)) and valor > 0


# -------------------------------------------------------

# Ejemplo de uso
mi_lista = ListaPositiva()
mi_lista.append(10)
mi_lista.extend([1, 2, 3])
mi_lista.insert(1, 4)
mi_lista[0] = 99  # Asignación directa
print(mi_lista)  # Salida: [99, 4, 1, 2, 3]

# Esto generará errores:
mi_lista.append(-1)
mi_lista.extend([1, -2])
# mi_lista[0] = -5

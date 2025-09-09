
from collections import Counter, deque, namedtuple, defaultdict, OrderedDict

# 1. Counter: cuenta la frecuencia de elementos en una lista o iterable
frutas = ['manzana', 'banana', 'manzana', 'pera', 'banana', 'manzana']
contador = Counter(frutas)
print("Frecuencia de frutas:", contador)
print("Las 2 frutas más comunes:", contador.most_common(2))

# 2. deque: lista doblemente terminada, eficiente para añadir o quitar elementos al inicio o final
cola = deque(['a', 'b', 'c'])
cola.append('d')        # Añadir al final
cola.appendleft('z')    # Añadir al inicio
print("Contenido de deque:", cola)
cola.pop()              # Quitar del final
cola.popleft()          # Quitar del inicio
print("Deque tras pop y popleft:", cola)

# 3. namedtuple: crea una tupla con nombres para acceder a sus campos
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])
p = Persona(nombre='Ana', edad=30, ciudad='Madrid')
print("Persona:", p)
print("Nombre:", p.nombre)

# 4. defaultdict: diccionario que asigna un valor por defecto si la clave no existe
dd = defaultdict(int)  # Valor por defecto es 0 (int)
dd['manzanas'] += 1
dd['naranjas'] += 2
print("Defaultdict con conteos:", dd)

# 5. OrderedDict: diccionario que recuerda el orden en que se insertan los elementos
od = OrderedDict()
od['primero'] = 1
od['segundo'] = 2
od['tercero'] = 3
print("OrderedDict:", od)
print("Claves en orden:", list(od.keys()))

print("\nFin del script collections.")

# Este ejemplo sera un ejemplo de codificacion y decodificacion de un archivo

from json import dumps, loads

miDiccionario = {
        'hola':[1,2,3],
        'contenido':[11,22,33]
        }

# Codificar objeto a cadena de texto
codificado = dumps(miDiccionario)

# Escribir cadenas de texto
with open('archivo.json','w') as file:
    file.write(codificado)  
    print('archivo.json -->  generado')

# Leer cadenas de texto
with open('archivo.json','r') as file:
    contenido= file.read()
    print('archivo.json -->  leido')

# Decodificar cadena de texto a objeto
decodificado = loads(contenido)

# ultimo paso comparando objeto y objeto recuperado

print(miDiccionario) # objeto original
print(decodificado)  # objeto  


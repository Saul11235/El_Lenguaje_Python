# Este ejemplo sera un ejemplo de codificacion y decodificacion de un archivo

from csv import reader,writer

datos = [
    ['nombre', 'edad', 'Lenguaje'   ],
    ['Ana'   , 30    , 'python'     ],
    ['Luis'  , 25    , 'javascript' ],
    ['Sofía' , 28    , 'java'       ]
]

#texto Escribir archivo csv
with open('archivo.csv','w',encoding="utf-8",newline='') as file:
    writer(file).writerows(datos)
    print('archivo.csv -->  generado')

# Decodificar archivo de texto
with open('archivo.csv','r',encoding="utf-8") as file:
    contenido= list(reader(file))
    print('archivo.csv -->  leido')

# ultimo paso comparando objeto y objeto recuperado

print(datos)         # objeto original
print(contenido)     # objeto  


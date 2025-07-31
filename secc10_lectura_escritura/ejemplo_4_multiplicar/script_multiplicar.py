#
# TABLAS DE MULTIPLICAR CSV
#
# Cree un programa python que en base a números 
# enteros leídos por el usuario renderize varios 
# archivos CSV, estos serán tablas de multiplicar 
# de números enteros en un rango determinado por el usuario.
#
# ---------------------------------------------

from csv import writer

# ---------------------------------------------

def input_default(str_input,default):
    'input con un valor por defecto'
    string = input(str_input)
    try    : return int(string)
    except : return default

# ---------------------------------------------

def escribir_archivo_CSV(minimo,maximo,actual):
    nombre =  f'tabla_{actual}.csv'
    datos  = [[f'tabla multiplicar del {actual}'],[]]
    for x in range(minimo,maximo):
        datos.append(['',actual,'x',x,'=',actual*x])
    with open(nombre,'w',encoding='utf-8',newline='') as file:
        writer(file).writerows(datos)
    print(f'{nombre} --> generado')

# ---------------------------------------------
# recopilando variable y construyendo archivos CSV

input('\n Generar tablas de Multiplicar \n')
minimo = input_default(' Iniciar en  : ', 0  )
maximo = input_default(' Terminar en : ', 13 )

for x in range(minimo,maximo):
    escribir_archivo_CSV(minimo,maximo,x)


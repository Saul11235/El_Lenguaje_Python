# ejemplo de lectura y escritura

cadena1="""

 Esta es una cadena con un dibujo

  ███████████████████ 
  ██               ██  
  ██    ██   ██    ██  
  ██    ██   ██    ██  
  ██               ██  
  ██   ██     ██   ██  
  ██     █████     ██  
  ██               ██  
  ███████████████████ 

"""

# escribiendo archivo
with open("archivo.txt","w",encoding="utf-8") as file:
    file.write(cadena1)

# leyendo archivo
with open("archivo.txt","r",encoding="utf-8") as file:
    cadena2=file.read()

# imprimiendo cadenas
print(cadena1)
print(cadena2)



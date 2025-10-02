
import tkinter 
import random
import string

# Función para generar clave aleatoria segura
def generar_clave():
    longitud = 12  # longitud de la clave
    caracteres = string.ascii_letters + string.digits + string.punctuation
    clave = ''.join(random.choice(caracteres) for _ in range(longitud))
    entry_clave.delete(0, tkinter.END)
    entry_clave.insert(0, clave)

# Crear ventana principal
root = tkinter.Tk()
root.title("Generador de Claves Aleatorias")

# Entry para mostrar la clave (solo lectura)
entry_clave = tkinter.Entry(root, width=40, font=("Helvetica", 14))
entry_clave.grid(row=0, column=0, padx=10, pady=10)

# Botón para generar clave
boton_generar = tkinter.Button(root, text="Generar clave", command=generar_clave, font=("Helvetica", 12))
boton_generar.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()

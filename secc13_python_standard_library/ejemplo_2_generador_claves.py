
import tkinter as tk
import secrets
import string

# Función para generar clave aleatoria segura
def generar_clave():
    longitud = 12  # longitud de la clave
    caracteres = string.ascii_letters + string.digits + string.punctuation
    clave = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    entry_clave.delete(0, tk.END)
    entry_clave.insert(0, clave)

# Crear ventana principal
root = tk.Tk()
root.title("Generador de Claves Aleatorias")

# Entry para mostrar la clave (solo lectura)
entry_clave = tk.Entry(root, width=40, font=("Helvetica", 14))
entry_clave.grid(row=0, column=0, padx=10, pady=10)

# Botón para generar clave
boton_generar = tk.Button(root, text="Generar clave", command=generar_clave, font=("Helvetica", 12))
boton_generar.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()

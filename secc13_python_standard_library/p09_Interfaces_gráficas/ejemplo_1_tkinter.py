
import tkinter as tk

# Función que se ejecuta al presionar el botón
def saludar():
    nombre = entrada.get()
    etiqueta_saludo.config(text=f"Hola, {nombre}!")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo tkinter")
ventana.geometry("300x150")

# Campo de texto
entrada = tk.Entry(ventana)
entrada.pack(pady=10)

# Botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Etiqueta de saludo
etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.pack(pady=10)

# Iniciar el bucle de eventos
ventana.mainloop()

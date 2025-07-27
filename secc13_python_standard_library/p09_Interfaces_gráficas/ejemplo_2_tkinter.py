
import tkinter as tk

# Inicializar el contador
contador = 0

# Función para incrementar el contador
def incrementar():
    global contador
    contador += 1
    etiqueta.config(text=f"Contador: {contador}")

# Función para reiniciar el contador
def reiniciar():
    global contador
    contador = 0
    etiqueta.config(text=f"Contador: {contador}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Contador")
ventana.geometry("250x150")

# Etiqueta que muestra el valor del contador
etiqueta = tk.Label(ventana, text=f"Contador: {contador}", font=("Arial", 14))
etiqueta.pack(pady=10)

# Botón para incrementar
boton_incrementar = tk.Button(ventana, text="Incrementar", command=incrementar)
boton_incrementar.pack()

# Botón para reiniciar
boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar)
boton_reiniciar.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()

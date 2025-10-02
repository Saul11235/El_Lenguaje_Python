import tkinter 
from   time    import strftime

# Crear ventana principal
root = tkinter.Tk()
root.title("Reloj Digital")

# Crear etiqueta para mostrar la hora
label_hora = tkinter.Label(root, font=("Helvetica", 48), bg="black", fg="cyan")
label_hora.pack(padx=20, pady=20)

# Función para actualizar la hora
def actualizar_reloj():
    hora_actual = strftime("%H:%M:%S")  # Formato de hora: HH:MM:SS
    label_hora.config(text=hora_actual)
    label_hora.after(1000, actualizar_reloj)  # Llama a esta función cada 1000 ms (1 segundo)

# Iniciar actualización
actualizar_reloj()

# Ejecutar la aplicación
root.mainloop()

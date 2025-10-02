
import tkinter 
from   math import sin, cos, tan, radians

def calcular_trigonometria():
    try:
        # Obtener el ángulo en grados desde el Entry y convertir a float
        angulo_grados = float(entry_angulo.get())
        angulo_radianes = radians(angulo_grados)  # Convertir a radianes

        # Calcular seno, coseno y tangente
        seno = sin(angulo_radianes)
        coseno = cos(angulo_radianes)
        tangente = tan(angulo_radianes)

        # Actualizar labels con resultados formateados
        label_seno_valor.config(text=f"{seno:.4f}")
        label_coseno_valor.config(text=f"{coseno:.4f}")
        label_tangente_valor.config(text=f"{tangente:.4f}")

    except ValueError:
        # Si no es un número válido, limpiar resultados
        label_seno_valor.config(text="Error")
        label_coseno_valor.config(text="Error")
        label_tangente_valor.config(text="Error")

# Crear ventana principal
root = tkinter.Tk()
root.title("Calculadora de Funciones Trigonométricas")

# Etiqueta y entrada para ángulo
tkinter.Label(root, text="Ángulo (grados):").grid(row=0, column=0, padx=10, pady=10)
entry_angulo = tkinter.Entry(root)
entry_angulo.grid(row=0, column=1, padx=10, pady=10)

# Botón para calcular
boton_calcular = tkinter.Button(root, text="Calcular", command=calcular_trigonometria)
boton_calcular.grid(row=0, column=2, padx=10, pady=10)

# Labels para mostrar resultados
tkinter.Label(root, text="Seno:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
label_seno_valor = tkinter.Label(root, text="-")
label_seno_valor.grid(row=1, column=1, padx=10, pady=5, sticky="w")

tkinter.Label(root, text="Coseno:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
label_coseno_valor = tkinter.Label(root, text="-")
label_coseno_valor.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tkinter.Label(root, text="Tangente:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
label_tangente_valor = tkinter.Label(root, text="-")
label_tangente_valor.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Ejecutar app
root.mainloop()

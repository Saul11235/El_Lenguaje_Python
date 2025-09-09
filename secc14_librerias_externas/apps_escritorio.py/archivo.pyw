# Nota pyw, no muestra la consola


import tkinter as tk
from tkinter import messagebox

class SumaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sumador de Números")
        self.root.geometry("300x200")

        # Crear el widget de la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta para el primer número
        self.label1 = tk.Label(self.root, text="Número 1:")
        self.label1.pack(pady=5)

        # Campo de texto para el primer número
        self.num1_input = tk.Entry(self.root)
        self.num1_input.pack(pady=5)

        # Etiqueta para el segundo número
        self.label2 = tk.Label(self.root, text="Número 2:")
        self.label2.pack(pady=5)

        # Campo de texto para el segundo número
        self.num2_input = tk.Entry(self.root)
        self.num2_input.pack(pady=5)

        # Botón para realizar la suma
        self.suma_button = tk.Button(self.root, text="Sumar", command=self.sumar)
        self.suma_button.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.result_label = tk.Label(self.root, text="Introduce dos números para sumar")
        self.result_label.pack(pady=5)

    def sumar(self):
        try:
            # Obtener los valores de los campos de texto y sumarlos
            num1 = float(self.num1_input.get())
            num2 = float(self.num2_input.get())
            resultado = num1 + num2
            self.result_label.config(text=f"Resultado: {resultado}")
        except ValueError:
            # Si hay un error en los valores ingresados
            self.result_label.config(text="Por favor, ingresa números válidos.")
            messagebox.showerror("Error", "Ambos campos deben ser números válidos.")

# Configuración de la ventana principal
if __name__ == '__main__':
    root = tk.Tk()
    app = SumaApp(root)
    root.mainloop()

#
# ejemplo pyqt
#
#  pip instal PyQt5
#



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class SumaApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        # Crear el layout vertical
        layout = QVBoxLayout()
        
        # Crear los campos de texto para ingresar los números
        self.num1_input = QLineEdit(self)
        self.num1_input.setPlaceholderText("Número 1")
        
        self.num2_input = QLineEdit(self)
        self.num2_input.setPlaceholderText("Número 2")
        
        # Crear el botón que suma los números
        suma_button = QPushButton("Sumar", self)
        suma_button.clicked.connect(self.sumar)
        
        # Crear la etiqueta para mostrar el resultado
        self.result_label = QLabel("Introduce dos números para sumar", self)
        
        # Añadir los widgets al layout
        layout.addWidget(self.num1_input)
        layout.addWidget(self.num2_input)
        layout.addWidget(suma_button)
        layout.addWidget(self.result_label)
        
        # Establecer el layout para la ventana
        self.setLayout(layout)
        
        # Configurar la ventana
        self.setWindowTitle('Sumador de Números')
        self.setGeometry(100, 100, 300, 200)

    def sumar(self):
        try:
            # Obtener los valores ingresados y sumarlos
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            resultado = num1 + num2
            self.result_label.setText(f"Resultado: {resultado}")
        except ValueError:
            # Si hay un error en los valores (por ejemplo, si no son números válidos)
            self.result_label.setText("Por favor, ingresa números válidos.")

# Ejecutar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SumaApp()
    window.show()
    sys.exit(app.exec_())

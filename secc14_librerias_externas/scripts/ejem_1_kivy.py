#
#  ejemplo kivy instalar antes
#
#  pip install kivy
#
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SumaApp(App):
    def build(self):
        # Layout vertical
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Etiqueta para mostrar el resultado
        self.result_label = Label(text="Introduce dos números para sumar")
        
        # Crear campos de entrada de texto para los números
        self.num1_input = TextInput(hint_text="Número 1", multiline=False, input_filter='float')
        self.num2_input = TextInput(hint_text="Número 2", multiline=False, input_filter='float')
        
        # Crear un botón para realizar la suma
        suma_button = Button(text="Sumar")
        suma_button.bind(on_press=self.sumar)
        
        # Añadir los widgets al layout
        layout.add_widget(self.num1_input)
        layout.add_widget(self.num2_input)
        layout.add_widget(suma_button)
        layout.add_widget(self.result_label)
        
        return layout
    
    def sumar(self, instance):
        try:
            # Obtener los valores ingresados y sumarlos
            num1 = float(self.num1_input.text)
            num2 = float(self.num2_input.text)
            resultado = num1 + num2
            self.result_label.text = f"Resultado: {resultado}"
        except ValueError:
            # Si los valores no son válidos, mostrar un mensaje de error
            self.result_label.text = "Por favor, ingresa números válidos."

# Ejecutar la aplicación
if __name__ == '__main__':
    SumaApp().run()

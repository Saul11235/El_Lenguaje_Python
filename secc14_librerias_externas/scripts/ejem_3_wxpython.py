
import wx

class SumaApp(wx.Frame):
    def __init__(self, parent, title):
        super(SumaApp, self).__init__(parent, title=title, size=(300, 200))
        
        # Crear el panel principal
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Crear los campos de texto para ingresar los números
        self.num1_input = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.num1_input.SetHint("Número 1")
        
        self.num2_input = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.num2_input.SetHint("Número 2")
        
        # Crear el botón que realizará la suma
        suma_button = wx.Button(panel, label="Sumar")
        suma_button.Bind(wx.EVT_BUTTON, self.sumar)
        
        # Crear la etiqueta para mostrar el resultado
        self.result_label = wx.StaticText(panel, label="Introduce dos números para sumar")

        # Añadir widgets al layout
        vbox.Add(self.num1_input, flag=wx.EXPAND | wx.TOP, border=10)
        vbox.Add(self.num2_input, flag=wx.EXPAND | wx.TOP, border=10)
        vbox.Add(suma_button, flag=wx.EXPAND | wx.TOP, border=10)
        vbox.Add(self.result_label, flag=wx.EXPAND | wx.TOP, border=10)

        panel.SetSizer(vbox)
        
        # Mostrar la ventana
        self.Show()

    def sumar(self, event):
        try:
            # Obtener los valores de los campos de texto y sumarlos
            num1 = float(self.num1_input.GetValue())
            num2 = float(self.num2_input.GetValue())
            resultado = num1 + num2
            self.result_label.SetLabel(f"Resultado: {resultado}")
        except ValueError:
            # Si la conversión a float falla (por ejemplo, si no es un número válido)
            self.result_label.SetLabel("Por favor, ingresa números válidos.")

if __name__ == '__main__':
    app = wx.App(False)
    SumaApp(None, title="Sumador de Números")
    app.MainLoop()

#
# Ejemplo de cilindro
#

# declarando clase

class clase_cilindro:
    altura   =  0
    radio    =  0

    def calcula_area(self):
        pi           = 3.1415
        area_base    = pi * self.radio ** 2
        area_lateral = 2 * pi * self.radio * self.altura
        area_total   = 2 * area_base + area_lateral
        print("El área es", area_total)

    def calcula_volumen(self):
        pi     = 3.1415
        volumen = pi * self.radio ** 2 * self.altura
        print("El volumen es", volumen)


# creando cilindro y definiendo atributos
cilindro = clase_cilindro()

cilindro.altura = 10
cilindro.radio  = 8

# calculando
cilindro.calcula_area()
cilindro.calcula_volumen()


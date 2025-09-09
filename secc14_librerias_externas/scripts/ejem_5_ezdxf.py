# -------------------------------------------------------------
#
# Este ejemplo toma datos de usuario y crea un plano simple
# para instalar ezdxf
# 
#  pip install ezdxf
#
# -------------------------------------------------------------

import ezdxf

input("Rectangulo\n")

# Solicitar al usuario las dimensiones del rectángulo
largo = float(input("Introduce el largo del rectángulo: "))
ancho = float(input("Introduce el ancho del rectángulo: "))

# Calcular el perímetro y el área
perimetro = 2*(largo+ancho)
area      = largo*ancho

# Crear un nuevo documento DXF
dxf_doc = ezdxf.new(); msp=dxf_doc.modelspace()

# Dibujo
msp.add_lwpolyline(points=[(0, 0), (largo, 0), (largo, ancho), (0, ancho), (0, 0)],close=True)

# Colocar texto
msp.add_text(f"Largo: {largo}m",height=0.5).set_placement((0, -2))
msp.add_text(f"Ancho: {ancho}m",height=0.5).set_placement((0, -3))
msp.add_text(f"Perímetro: {perimetro}m",height=0.5).set_placement((0, -4))
msp.add_text(f"Area: {area}m2",height=0.5).set_placement((0, -5))

# Guardar archivo DXF
dxf_doc.saveas("rectangulo.dxf")



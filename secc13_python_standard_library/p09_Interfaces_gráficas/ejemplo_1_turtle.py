
import turtle

# Crear una ventana y una tortuga
ventana = turtle.Screen()
ventana.title("Ejemplo turtle")
ventana.bgcolor("white")

t = turtle.Turtle()
t.color("blue")
t.pensize(3)
t.speed(3)

# Dibujar un cuadrado
for _ in range(4):
    t.forward(100)
    t.right(90)

# Esperar al clic para cerrar
ventana.exitonclick()

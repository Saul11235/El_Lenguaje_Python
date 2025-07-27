import turtle

# Crear ventana
ventana = turtle.Screen()
ventana.title("Estrella con turtle")
ventana.bgcolor("black")

# Crear tortuga
t = turtle.Turtle()
t.color("yellow")
t.pensize(2)
t.speed(3)

# Dibujar estrella de 5 puntas
for _ in range(5):
    t.forward(150)
    t.right(144)

# Esperar clic para cerrar
ventana.exitonclick()

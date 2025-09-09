import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mover el Recuadro")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Posición y tamaño del recuadro
rect_width = 50
rect_height = 50
rect_x = screen_width // 2 - rect_width // 2
rect_y = screen_height // 2 - rect_height // 2
rect_speed = 5  # Velocidad de movimiento del recuadro

# Bucle principal del juego
clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)  # Rellenar la pantalla con color blanco

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()

    # Mover el recuadro según las teclas presionadas
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Asegurarse de que el recuadro no salga de los límites de la pantalla
    rect_x = max(0, min(screen_width - rect_width, rect_x))
    rect_y = max(0, min(screen_height - rect_height, rect_y))

    # Dibujar el recuadro
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de fotogramas
    clock.tick(60)

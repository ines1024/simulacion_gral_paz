import pygame
import sys
import time

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
window_width = 800
window_height = 200
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Animación de Puntos")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
point_color = (255, 0, 0)

# Longitud total de la línea (32,000 metros)
line_length = 32000

# Número de puntos
num_puntos = 5

# Velocidad de movimiento en metros por segundo
velocidad_metros_por_segundo = 100  # 100 metros por segundo

# Espaciado inicial entre los puntos
espaciado = 20

# Posiciones iniciales de los puntos
posiciones_x = [-i * espaciado for i in range(num_puntos)]

# Duración de la animación en segundos
duracion_animacion = 60  # Cambia esto a la duración deseada

# Reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()
# Tiempo de inicio de la animación
tiempo_inicio = time.time()

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcula el desplazamiento en función de la velocidad
    desplazamiento = velocidad_metros_por_segundo * reloj.get_time() / 1000.0  # Obtén el tiempo desde la última actualización

    # Mueve los puntos
    for i in range(num_puntos):
        posiciones_x[i] += desplazamiento

        # Si un punto llega al final de la línea, vuelve al inicio
        if posiciones_x[i] > window_width:
            posiciones_x[i] = -espaciado

    # Limpia la pantalla
    window.fill(white)

    # Dibuja la línea
    pygame.draw.line(window, black, (0, window_height // 2), (window_width, window_height // 2), 2)

    # Dibuja los puntos en sus nuevas posiciones
    for i in range(num_puntos):
        pygame.draw.circle(window, point_color, (int(posiciones_x[i]), window_height // 2), 3)


    # Actualiza la pantalla
    pygame.display.update()

    # Comprueba si la animación ha alcanzado la duración deseada y cierra la ventana
    tiempo_actual = time.time()
    if tiempo_actual - tiempo_inicio >= duracion_animacion:
        pygame.quit()
        sys.exit()

    # Limita la velocidad de actualización a 1 vez por segundo
    reloj.tick(1)


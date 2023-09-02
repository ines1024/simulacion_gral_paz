from class_specification import Carril, Auto
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pygame
import sys

 # iniciamos la simulacion ingresando de a 1 auto
 # t = 0

 # son 32 km

# armamos la simulación
#expresamos las velocidades en m/s
min_vel = 60/3.6
max_vel = 80/3.6
# inicializamos el primer auto
auto1: Auto = Auto(0, 0, 0, np.random.randint(min_vel, max_vel), 0)
autos: list[Auto] = [auto1]
i: int = 1
dist = 200

#inicializamos el carril (ponemos los autos en el lugar)
while (dist < 32000):
    vel = np.random.randint(min_vel, max_vel)
    auto_i: Auto = Auto(i, dist, 0, vel, 0) # id, pos, t, vel, acel
    autos.append(auto_i)
    i+=1
    dist += 200

########################## GRAFICO
# Inicializa Pygame
pygame.init()

# Configuración de la ventana
window_width = 1000
window_height = 200
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("General Paz")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
point_color = (255, 0, 0)

# Longitud total de la línea (32,000 metros)
line_length = 32000
#############################3

# iniciamos la simulacion con autos cada 200 metros
carril: Carril = Carril(autos)

# arranca el tiempo
t = 0

# Iniciar la simulación
carril = Carril(autos)
tiempo_total = 120  # Tiempo total de simulación en segundos

# Reloj para controlar la velocidad de actualización
reloj = pygame.time.Clock()
# Tiempo de inicio de la animación
tiempo_inicio = time.time()
        


# GRAFICO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpia la pantalla
    window.fill(white)

    # Dibuja la línea
    pygame.draw.line(window, black, (0, window_height // 2), (window_width, window_height // 2), 1)

    for auto in carril.autos:
        if (auto.fin == 0): # el auto todavia no termino
        # pensar ratio de vel ~ pos del de adelante (que define cuanto acelera)
            aceleracion = 0
            auto.pos += (auto.vel + aceleracion) * reloj.get_time() / 1000.0 # funciona supongo porque vel esta definida en metros por segundo
            auto.vel = auto.vel + aceleracion
            auto.t +=1

            pygame.draw.circle(window, (0, 0, 255), (int(auto.pos), window_height // 2), 2)

    # if t % 2 == 0:
    # # Agregar un nuevo auto cada dos segundos
    #     i_nuevo = len(carril.autos)
    #     nuevo_auto = Auto(i_nuevo, 0, t, np.random.randint(min_vel, max_vel), 0)
    #     carril.autos.append(nuevo_auto)
    #     pygame.draw.circle(window, (255, 0, 0), (int(nuevo_auto.pos), window_height // 2), 2)
        
    #     # Si un punto llega al final de la línea, sale del grafico
    #     if auto.pos > 32000:
    #         auto.fin = 1
            


    '''
    # Calcula el desplazamiento en función de la velocidad
    desplazamiento = velocidad_metros_por_segundo * reloj.get_time() / 1000.0  # Obtén el tiempo desde la última actualización

    # Mueve los puntos
    for i in range(num_puntos):
        posiciones[i] += desplazamiento[i]
    '''

        
    

    # Dibuja los puntos en sus nuevas posiciones
    #for i in range(len(carril.autos)):

    # Actualiza la pantalla
    pygame.display.update()

    # Comprueba si la animación ha alcanzado la duración deseada y cierra la ventana
    t +=1
    if t == tiempo_total:
        pygame.quit()
        sys.exit()

    # Limita la velocidad de actualización a 1 vez por segundo
    reloj.tick(1)


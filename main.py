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
auto1: Auto = Auto(0, 0, 0, np.random.randint(min_vel, max_vel), 0, 0.95, 0, 0)
autos: list[Auto] = [auto1]
i: int = 1
dist = 600

#inicializamos el carril (ponemos los autos en el lugar)
while (dist < 32000):
    vel = np.random.randint(min_vel, max_vel)
    p_acel = 0.95
    auto_i: Auto = Auto(i, dist, 0, vel, 0, p_acel, dist, 0) # id, pos, t, vel, acel
    autos.append(auto_i)
    i+=1
    dist += 600

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
escala = window_width / line_length
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
    
    i = 0
    for auto in carril.autos:
        if (auto.fin == 0): # el auto todavia no termino
        # pensar ratio de vel ~ pos del de adelante (que define cuanto acelera)
            if (i < len(carril.autos)-1):
                pos_adel = carril.adelante(i+1)[1]
                pos_adel_ant = carril.adelante(i+1)[0]
                auto.acelerar(pos_adel, pos_adel_ant)
                auto.pos_ant = auto.pos
                auto.pos += (auto.vel) * reloj.get_time() /1000.0

                if (auto.choque == 3):
                    auto.vel = 5
                    auto.choque = 0

                if (auto.choque > 0):
                    auto.choque -= 1
                    auto.vel = 0
                

                if auto.pos == pos_adel:
                    print("choque")
                    auto.choque = 3
                    auto.vel = 0

                if (i > 0): 
                    if (carril.autos[i-1].choque > 0):
                        if (carril.autos[i-1].choque == 3):
                            auto.vel = 0
                        else:
                            auto.vel = 5 * carril.autos[i-1]   
                                    
                
            # obs: hacer que el ultimo avance 
            auto.t +=1
            pos_en_ventana = int(auto.pos*escala)
            pygame.draw.circle(window, (0, 0, 255), (int(pos_en_ventana), window_height // 2), 2)
        i+=1

    # ARREGLAR 
    # if t % 2 == 0:
    # # Agregar un nuevo auto cada dos segundos
    #     i_nuevo = len(carril.autos)
    #     nuevo_auto = Auto(i_nuevo, 0, t, np.random.randint(min_vel, max_vel), 0)
    #     carril.autos.append(nuevo_auto)
    #     pygame.draw.circle(window, (255, 0, 0), (int(nuevo_auto.pos), window_height // 2), 2)
        
    #     # Si un punto llega al final de la línea, sale del grafico
    #     if auto.pos > 32000:
    #         auto.fin = 1

        
    

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


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
min_vel = 40/3.6
max_vel = 80/3.6

autos: list[Auto] = []
i: int = 0
dist = 14900

#inicializamos el carril (ponemos los autos en el lugar)
while (dist > 0):
    auto_i: Auto = Auto(i, dist, 0, 0, 0, dist, 0) # id, pos, t, vel, acel, pos_ant, choque
    auto_i.vel = auto_i.vel_prefe
    autos.append(auto_i)
    i+=1
    dist -= 100

# el primer auto de la lista es el mas cercano a llegar (id = 0)

########################## GRAFICO
# Inicializa Pygame
pygame.init()

# Configuración de la ventana
ancho_inicial = 1000
window_width = ancho_inicial 
window_height = 200
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("General Paz")


# Colores
white = (255, 255, 255)
black = (0, 0, 0)
verde = (0, 255, 0)
rojo = (255, 0, 0)
naranja = (255, 128, 0)

############################# SIMULACION

# iniciamos la simulacion con autos cada 200 metros
carril: Carril = Carril(autos)

# arranca el tiempo
t = 0

posicion_actual = 0

# Iniciar la simulación
carril = Carril(autos)
tiempo_total = 86400  # Tiempo total de simulación en segundos

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                posicion_actual -= 1000  # Mueve 100 metros a la izquierda
            elif event.key == pygame.K_RIGHT:
                posicion_actual += 1000  # Mueve 100 metros a la derecha
                
    # Asegúrate de que la posición actual esté dentro de los límites del tramo
    posicion_actual = max(0, min(15000 - window_width, posicion_actual))

    # Actualiza el ancho de la ventana según la posición actual
    window_width = 1000  # Ancho fijo de la ventana
    tramo_visible = (posicion_actual, posicion_actual + window_width)

    # Limpia la pantalla
    window.fill(white)

    # Dibuja la línea
    pygame.draw.line(window, black, (0, window_height // 2), (window_width, window_height // 2), 30)
    
    i = 0
    for auto in carril.autos:

        if (auto.fin == 0): # el auto todavia no termino

            if (i == 0): 
                # es el ultimo auto (no tiene adelante)
                auto.acelerar(20000)
                auto.pos_ant = auto.pos
                auto.pos += (auto.vel) * reloj.get_time() /1000.0


            elif (i < len(carril.autos)):
                if carril.autos[i-1].fin == 1:
                    # el de adelante ya salio
                    pos_adel = 20000
                else: 
                    pos_adel = carril.autos[i-1].pos # id del de adelante es i-1
                auto.acelerar(pos_adel)
                auto.pos_ant = auto.pos
                auto.pos += (auto.vel) * reloj.get_time() /1000.0

                # el auto salio
                if (auto.pos) >= 15000:
                    auto.fin == 1
                    if (i > 15):
                        print("salio:", i, ", tardo:", t-auto.t_inicio)

                #CHOQUE
                if (auto.choque > 0):
                    auto.choque = 0
                
                if auto.pos >= pos_adel and pos_adel < 15000:
                    #chequeamos que el de adelante no haya ya salido
                    print("____________________________________________")
                    print("choque del auto", i,"a ", i-1, ",en t=", t)
                    print("____________________________________________")
                    auto.choque = 1
                    auto.vel = 0
                    carril.autos[i-1].vel = 0

                 
                # if (carril.autos[i+1].choque > 0): 
                #     # el de atras me choco
                #     auto.vel = 0  

                if auto.vel > 81/3.6 and (auto.pos_ant < 5500 and auto.pos >= 5500): 
                    auto.multas +=1
                    #print("multa a", auto.vel*3.6)
                    #print("multa 1", auto.vel*3.6, "prefe:", auto.vel_prefe*3.6)

                if auto.vel > 81/3.6 and (auto.pos_ant < 10500 and auto.pos >= 10500): 
                    auto.multas +=1
                    #print("multa 2", auto.vel*3.6, auto.id) 

                # if auto.pos_ant < 5500 and auto.pos >= 5500:
                #     print("CAMARA a", auto.vel*3.6, ", prefe", auto.vel_prefe*3.6)
                # if auto.pos_ant < 3000 and auto.pos >= 3000:
                #     print("OTRO a", auto.vel*3.6, ", prefe", auto.vel_prefe*3.6)
                           
                
            
            # obs: hacer que el ultimo avance 
            auto.t +=1
            # pos_en_ventana = int(auto.pos*escala)
            # pygame.draw.circle(window, point_color, (int(pos_en_ventana), window_height // 2), 3)
            if tramo_visible[0] <= auto.pos <= tramo_visible[1]:
                pos_en_ventana = int(auto.pos - tramo_visible[0])
                if auto.choque > 0:
                    pygame.draw.circle(window, rojo, (pos_en_ventana, window_height // 2), 3)
                else:
                    pygame.draw.circle(window, verde, (pos_en_ventana, window_height // 2), 3)
        i+=1

        # Regulamos la densidad del trafico (metemos nuevos autos)
        if ((t in range(7*3600, 11*3600) or t in range(16*3600, 20*3600)) and t % 3 == 0 and carril.autos[len(carril.autos)-1].pos > 30) or (t % 30 == 0 and carril.autos[len(carril.autos)-1].pos > 30): 
            # Agrega un nuevo auto 
            i_nuevo = len(carril.autos)

            if carril.autos[len(carril.autos)-1].pos > 200:
                vel = random.normalvariate(80/3.6, 15/3.6)
            elif carril.autos[len(carril.autos)-1].pos > 60:
                vel = random.normalvariate(80/3.6, 10/3.6)
            else: 
                vel = random.normalvariate(30/3.6, 10/3.6)

            nuevo_auto = Auto(i_nuevo, 0, t, vel, 0, 0, 0)
            carril.autos.append(nuevo_auto)
            pygame.draw.circle(window, (255, 0, 0), (int(nuevo_auto.pos- tramo_visible[0]), window_height // 2), 3)
            
        # Graficamos la posicion de las camaras
        pygame.draw.circle(window, naranja, (int(5500- tramo_visible[0]), window_height // 2), 3.5)
        pygame.draw.circle(window, naranja, (int(10500- tramo_visible[0]), window_height // 2), 3.5)
    # imprimimos el tiempo
    if (t%3600 == 0):
        print(t/3600)


    # Actualiza la pantalla
    pygame.display.update()

    # Comprueba si la animación ha alcanzado la duración deseada y cierra la ventana
    t +=1
    if t == tiempo_total:
        pygame.quit()
        sys.exit()

    # Limita la velocidad de la animación a 100 fotogramas por segundo
    reloj.tick(10000) 


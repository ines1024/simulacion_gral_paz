from class_specification import Carril, Auto
import random
import time
import numpy as np
import matplotlib.pyplot as plt

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


# iniciamos la simulacion con autos cada 200 metros
carril: Carril = Carril(autos)

# arranca el tiempo
t = 0
tiempo_total = 60

for seg in range(tiempo_total):
    for auto in carril.autos:
        if (auto.fin == 0): # el auto todavia no termino
        # pensar ratio de vel ~ pos del de adelante (me define cuanto acelero)
            aceleracion = 0
            auto.pos += auto.vel * aceleracion
            #porque vel esta definida en metros por segundo
            auto.t = seg
    
    if seg // 2 == 0: 
        i_nuevo = len(carril.autos)
        # agrego auto cada dos segundos
        nuevo_auto: Auto = Auto(i_nuevo, 0, seg, np.random.randint(min_vel, max_vel), 0)
        carril.autos.append(nuevo_auto)


    # esto me dijo GPT, ignorenlo xd 
    plt.scatter(range(tiempo_total), [0] * len(carril.autos), c='gray', marker='o', s=100)  # Carril
    plt.scatter(range(tiempo_total), [0.5] * len(carril.autos), c='blue', marker='o', s=100)  # Autos
    plt.title(f'Segundo {seg + 1}')
    plt.savefig(f'segundo_{seg + 1}.png')  # Guarda la imagen de cada segundo
    plt.clf()  # Limpia la gráfica para el siguiente segundo
    time.sleep(1)  # Espera 1 segundo antes del próximo segundo

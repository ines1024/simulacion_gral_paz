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

'''
fig, ax = plt.subplots()
plt.xlabel('Distancia (metros)')
plt.ylabel('Tiempo (segundos)')

posiciones = [[] for _ in range(len(carril.autos))]  # Lista de listas para las posiciones
tiempos = [[] for _ in range(len(carril.autos))]     # Lista de listas para los tiempos
'''

for seg in range(tiempo_total):
    for auto in carril.autos:
        if (auto.fin == 0): # el auto todavia no termino
        # pensar ratio de vel ~ pos del de adelante (que define cuanto acelera)
            aceleracion = 0 # -1 < a < 1 (-1 es clavar los frenos)
            auto.pos += auto.vel * aceleracion # funciona supongo porque vel esta definida en metros por segundo
            auto.t = seg
        
    '''
    # Guarda la posición y el tiempo en las listas correspondientes (para graficar)
    posiciones[auto.id].append(auto.pos)
    tiempos[auto.id].append(auto.t)
    '''
    
    if seg % 2 == 0: 
        i_nuevo = len(carril.autos)
        # agrego auto cada dos segundos
        nuevo_auto: Auto = Auto(i_nuevo, 0, seg, np.random.randint(min_vel, max_vel), 0)
        carril.autos.append(nuevo_auto)

    time.sleep(1)
        
    '''  
    # Graficar la posición de los autos en el carril
    for i in range(len(carril.autos)):
        if carril.autos[i].fin==0:
            plt.scatter(posiciones[i], tiempos[i], label=f'Auto {i + 1}', s=20)


    plt.legend()
    '''

'''
plt.show()
'''

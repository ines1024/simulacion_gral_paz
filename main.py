from class_specification import Carril, Auto
import random
import numpy as np

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
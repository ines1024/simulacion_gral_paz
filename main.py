from class_specification import Carril, Auto
import random
import numpy as np

 # iniciamos la simulacion ingresando de a 1 auto
 # t = 0

 # son 32 km

# armamos la simulación
dist = 0
t = 0 #????

# inicializamos el primer auto
auto1: Auto = Auto(0, 0, t, np.random.randint(60, 80), 0, np.random.randint(60, 80), np.random.randint(60, 80), 200, -200)
autos: list[Auto] = [auto1]
i: int = 1
dist = 200

#inicializamos el carril (ponemos los autos en el lugar)
while (dist < 32000):
    vel_ad = np.random.randint(60, 80)
    auto_i: Auto = Auto(i, dist, t, autos[i-1].auto_ad[0], 0, vel_ad, autos[i-1].vel[0], dist+200, dist-200)
   # id:int, p:int, t:int, v:int, a:int, v_ad:int, v_at:int, p_ad:int, p_at:int)
    autos.append(auto_i)
    i+=1
    dist += 200


sim: Carril = Carril(autos)
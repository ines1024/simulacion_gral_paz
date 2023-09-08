# Atributos: 
# ID: número identificador de auto (3 dígitos numéricos)
# {pos, temp} → posición p en tiempo t, metros
# {vel, temp} → velocidad v en tiempo t, metros/segundo
# {acel, temp} → aceleración a en tiempo t, metros/segundo
# {vel_ad, temp} → velocidad auto de adelante en tiempo t
# {vel_at, temp} → velocidad auto de atrás en tiempo t
import random 
import numpy as np


class Auto:
    def __init__(self, id:int, p:int, t:int, v:int, a:int, p_ant, choque):
        self.id = id
        self.pos = p
        self.t_inicio = t # guardamos tiempo de entrada porque el de salida es el que queda guardado
        self.t = t
        self.vel = v
        self.acel = a
        self.fin = 0
        self.pos_ant = p_ant
        self.choque = 0

        #randomizamos la personalidad (proba de que acelere o se mantenga)
        rand = random.randint(0, 5)
        if rand == 1:
            self.media_acel = 0.3 #lento
        elif rand == 2:
            self.media_acel = 1.5 #rapido
        else: 
            self.media_acel = 1 #promedio

        rand2 = random.randint(0, 5)
        if rand2 == 1:
            self.distraido = 0.1
        elif rand2 == 2:
            self.distraido = 0.7
        else: 
            self.distraido = 0.3 #promedio
        
        

    def __repr__ (self):
        return str(self.__dict__)
    

    def final_recorrido(self):
        self.fin = 1
    

    def acelerar(self, pos_adel, pos_adel_ant):
        '''un auto puede acelerar entre -4 y 2'''

        distancia_ant = pos_adel_ant - self.pos_ant
        distancia = pos_adel - self.pos
        val_aceleracion = 0
        
        if (self.t == 0): 
            distancia_ant = 0
        
        # dif < 0 : me estoy acercando
        # dif > 0 : me estoy alejando
        dif = distancia - distancia_ant


        if(distancia >= 400): # re lejos
            # esta lejos
                val_aceleracion = random.normalvariate(self.media_acel, 0.5)


        elif(distancia >= 100): # distancia por encima de lo recomendado
            if (dif < 0):
                # me estoy acercando
                val_aceleracion = random.normalvariate(self.media_acel-0.5, 0.5)
            else: 
                # me estoy alejando del de adelante
                val_aceleracion = random.normalvariate(self.media_acel, 0.2)

            
        else: 
            # distancia por debajo de lo recomendado                 
            # reacciona?...
            azar = random.randint(0, 1)
            if azar < self.distraido:
                #no
                val_aceleracion = random.normalvariate(-3, 1) # Calcular si llega a frenar!!!!!? GIO                else:
                #si
                val_aceleracion = random.normalvariate(-2, 2) # no depende de si suele acelerar, va a frenar por seguridad
        
        if(self.vel + val_aceleracion > 80/3.6):   # esta yendo a mas de la maxima
            if self.pos in range(4900, 5000) or self.pos in range(9900, 10000):
                val_aceleracion = -4 
                # meter distraccion
            else: 
                if val_aceleracion > 0:
                    # meter distraccion
                    val_aceleracion = -val_aceleracion

        if self.vel < 0:
            self.vel = 0

        self.acel = val_aceleracion
        self.vel = self.vel + self.acel

        # chequear choque
        # dist en t - dist en (t-1) --> % de que tanto me estoy acrecando
        # conductores con distintas probas de acercarse 
        # desacelerar si estoy muy cerca de la vel maxima 
        

         # # Calcular la desaceleración necesaria para evitar una colisión
            # desaceleracion = (self.vel**2 - vel_adel**2) / (2 * distancia)

            # # Introducimos aleatoriedad en el tiempo de reacción
            # tiempo_reaccion = random.normalvariate(2, 0.5)

            # # Calcular la probabilidad de choque
            # probabilidad_choque = calcular_probabilidad_choque(desaceleracion, tiempo_reaccion)

            # # Simular si ocurre un choque
            # if random.random() < probabilidad_choque:
            #     print("¡Choque!")
            # else:
            #     # Aplicar la desaceleración y actualizar la velocidad
            #     self.velocidad -= desaceleracion

        


class Carril:
    def __init__(self, autos:list[Auto]):
        self.autos = autos
        

    def adelante(self, i):
        # i es el id de el de adelante
        if self.autos[i].fin == 1:
            # el de adelante ya salio
            return 100000
        pos_ant = self.autos[i].pos_ant
        pos = self.autos[i].pos
        # devuelve los valores del de adelante
        return (pos_ant, pos)
    
    def atras(self, i):
        if i == len(self.autos)-1:
            # es el ultimo que entro
            return (-1000, -100000)
        pos_ant = self.autos[i].pos_ant
        pos = self.autos[i].pos
        # devuelve los valores del de atras
        return (pos_ant, pos)
    
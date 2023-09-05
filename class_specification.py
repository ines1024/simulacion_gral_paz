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
    def __init__(self, id:int, p:int, t:int, v:int, a:int, p_acel, p_ant, choque):
        self.id = id
        self.pos = p
        self.t_inicio = t # guardamos tiempo de entrada porque el de salida es el que queda guardado
        self.t = t
        self.vel = v
        self.acel = a
        self.fin = 0
        self.prob_acel = p_acel
        self.pos_ant = p_ant
        self.choque = 0
        

    def __repr__ (self):
        return str(self.__dict__)
    
    def final_recorrido(self):
        self.fin = 1
    
    def acelerar(self, pos_adel, pos_adel_ant):
        '''un automóvil promedio puede acelerar en el rango de 4.9 m/s² a 9.8 m/s² en condiciones normales
        --> puede aumentar su velocidad en 4.9 m/s o más en un segundo.
        '''

        distancia_ant = pos_adel_ant - self.pos_ant
        distancia = pos_adel - self.pos
        
        if (self.t == 0): 
            distancia_ant = 0
        
        
        
        # dif < 0 : me estoy acercando
        # dif > 0 : me estoy alejando
        dif = distancia - distancia_ant


        # ???????? vel = vel + media * "t" + sqrt("t") * Z~N(0,1)

        if(distancia >= 200): 
            #esta muy lejos, no importa si ya estaba avanzando
            val_aceleracion = random.normalvariate(4, 1)
        
        elif(distancia >= 100):
            if (dif > 20):  # me estoy alejando mucho
                val_aceleracion = random.normalvariate(3, 1)
            elif (dif > 0): 
                val_aceleracion = random.normalvariate(2, 1)

            elif (dif < -20): 
                val_aceleracion = random.normalvariate(-1, 1)
            elif (dif < 0): 
                val_aceleracion = random.normalvariate(1, 1)
            
        elif(distancia >= 60): 
            if (dif > 20):
                val_aceleracion = random.normalvariate(1, 1)
            elif (dif > 0): 
                val_aceleracion = random.normalvariate(-1, 1)

            elif (dif < -20): 
                val_aceleracion = random.normalvariate(-3, 1)
            elif (dif < 0): 
                val_aceleracion = random.normalvariate(-2, 1)

        elif (distancia >= 30): 
            val_aceleracion = random.normalvariate(-7, 2)

        else: 
            val_aceleracion = -10  # desacelera lo maximo que puede 
        
        if(self.vel > 80/3.6):   # esta yendo a la maxima
            val_aceleracion = random.normalvariate(-1, 1)
        
        if(self.vel == 80/3.6):   
            val_aceleracion = 0

        if random.random() < self.prob_acel: #decide si acelerar o no
        # Calcula la aceleración en función del factor de aceleración máximo
            self.acel = val_aceleracion
            self.vel = self.vel + self.acel

        if self.vel < 0:
            self.vel = 0

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
    
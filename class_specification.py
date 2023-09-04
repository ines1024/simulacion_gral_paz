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
    def __init__(self, id:int, p:int, t:int, v:int, a:int):
        self.id = id
        self.pos = p
        self.t_inicio = t # guardamos tiempo de entrada porque el de salida es el que queda guardado
        self.t = t
        self.vel = v
        self.acel = a
        self.fin = 0
        

    def __repr__ (self):
        return str(self.__dict__)
    
    def final_recorrido(self):
        self.fin = 1
    
    def acelerar(self, pos_adel, vel_adel):
        '''un automóvil promedio puede acelerar en el rango de 4.9 m/s² a 9.8 m/s² en condiciones normales
        --> puede aumentar su velocidad en 4.9 m/s o más en un segundo.
        '''

        prob_acel = -1

        distancia = pos_adel - self.pos
        print(distancia)

        if(self.vel == 80/3.6):   #esta yendo a la máxima
            prob_acel = 0.0 #nota: le agregaria una chance muy pequeña porq hay gente que se zarpa
            val_aceleracion = 0
        
        if(distancia >= 200): 
            prob_acel = random.uniform(0.8, 1)
            val_aceleracion = random.normalvariate(4, 1)
        
        elif(distancia >= 100): 
            prob_acel = random.uniform(0.6, 0.8)
            val_aceleracion = random.normalvariate(3, 1)
            
        elif(distancia >= 60): #chances de que frene
            prob_acel = random.uniform(0.0, 1.0)
            if random.random() < 0.5:
                #frena
                val_aceleracion = -random.normalvariate(1, 1)   
            else:
                #acelera 
                val_aceleracion = random.normalvariate(1, 1) 

        else:
            prob_acel = 1.0
            val_aceleracion = random.normalvariate(-3, 2)
            
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

        
        if random.random() < prob_acel: #decide si acelerar o no
        # Calcula la aceleración en función del factor de aceleración máximo
            self.acel = val_aceleracion
            self.vel = self.vel + self.acel

        
        


class Carril:
    def __init__(self, autos:list[Auto]):
        self.autos = autos
        

    def adelante(self, i):
        # i es el id de el de adelante
        if self.autos[i].fin == 1:
            # el de adelante ya salio
            return 100000
        v = self.autos[i].vel
        p = self.autos[i].pos
        # devuelve los valores del de adelante
        return (v, p)
    
    def atras(self, i):
        if i == len(self.autos)-1:
            # es el ultimo que entro
            return (-1000, -100000)
        v = self.autos[i].vel
        p = self.autos[i].pos
        # devuelve los valores del de atras
        return (v, p)
    
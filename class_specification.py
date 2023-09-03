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
        self.t = t
        self.vel = v
        self.acel = a
        self.fin = 0
        # guardar tiempo de entrada? porque el de salida se guarda en el main

    def __repr__ (self):
        return str(self.__dict__)
    
    def final_recorrido(self):
        self.fin = 1
    
    def acelerar(self, p):
        prob_acel = -1
        if(self.vel == 80/3.6):
            prob_acel = 0.0
            val_aceleracion = 0
        
        if(p - self.pos >= 50):
            prob_acel = 1.0
            val_aceleracion = 0.15 * self.vel 

        elif(p-self.pos >= 30):
            prob_acel = 0.6
            val_aceleracion = 0.05 * self.vel 

        elif(p-self.pos >= 20):
            prob_acel = 0.0
            val_aceleracion = 0.0
        

        if random.random() < prob_acel: #decide si acelerar o no
        # Calcula la aceleración en función del factor de aceleración máximo
            self.acel = val_aceleracion # Puedes ajustar el 10.0 según tus necesidades
            self.vel = self.vel + self.acel
        


class Carril:
    def __init__(self, autos:list[Auto]):
        self.autos = autos
        
    def adelante(self, i):
        print(i)
        if self.autos[i-1].fin == 1:
            # el de adelante ya salio
            return 100000
        v = self.autos[i-1].vel
        p = self.autos[i-1].pos
        print(p)
        return p
    
    def atras(self, i):
        if i == len(self.autos)-1:
            # es el ultimo que entro
            return (-1000, -100000)
        v = self.autos[i+1].vel
        p = self.autos[i+1].pos
        return (v, p)
    
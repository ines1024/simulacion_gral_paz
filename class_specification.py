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
        self.multas = 0

        # media de velocidad que le gusta ir 
        rand = random.randint(0, 5)
        if rand == 1: #lento
            self.vel_prefe = random.normalvariate(65/3.6, 5/3.6)
        elif rand == 2 or rand == 3: #rapido
            self.vel_prefe = random.normalvariate(85/3.6, 5/3.6) 
        else: 
            self.vel_prefe = random.normalvariate(75/3.6, 5/3.6) 

        #randomizamos la personalidad (proba de que acelere o se mantenga)
        rand1 = random.randint(0, 5)
        if rand1 == 1:
            self.media_acel = 0.3 #lento
        elif rand1 == 2:
            self.media_acel = 1 #rapido
        else: 
            self.media_acel = 0.5 #promedio

        # distraccion
        rand2 = random.randint(0, 5)
        if rand2 == 1:
            self.distraido = 0.5
        elif rand2 == 2:
            self.distraido = 0.1
        else: 
            self.distraido = 0 #promedio
        
        

    def __repr__ (self):
        return str(self.__dict__)
    

    def final_recorrido(self):
        self.fin = 1
    

    def acelerar(self, pos_adel):
        '''un auto puede acelerar entre -4 y 2'''

        distancia = pos_adel - self.pos
        val_aceleracion = 0
        
        # dif < 0 : me estoy acercando
        # dif > 0 : me estoy alejando
        if (self.vel == 0):
            if (distancia < 10):
                self.vel = 0
            else: 
                self.vel = 3 #avanzo poco 
        
        else: 
            dif = distancia / self.vel

            if(dif > 2):
                # esta lejos
                #if (self.vel < self.vel_prefe):
                #val_aceleracion = random.normalvariate(self.media_acel+1, 0.5)
                if (self.vel_prefe > 80/3.6 and self.vel < 85/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel+0.5, 0.5)
                elif (self.vel_prefe > 80/3.6 and self.vel > 90/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel-1.5, 1)
                elif (self.vel_prefe < 80/3.6 and self.vel > 80/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel-1.2, 0.5)
                elif (self.vel_prefe < 80/3.6 and self.vel < 80/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel+0.3, 0.7)

            elif(dif > 1): # distancia por encima de lo recomendado
                #if (self.vel < self.vel_prefe):
                #val_aceleracion = random.normalvariate(self.media_acel+0.5, 0.5)
                if (self.vel_prefe > 80/3.6 and self.vel < 85/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel+0.3, 0.7)
                elif (self.vel_prefe > 80/3.6 and self.vel > 85/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel-2.5, 1)
                elif (self.vel_prefe < 80/3.6 and self.vel > 80/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel-3, 1)
                elif (self.vel_prefe < 80/3.6 and self.vel < 80/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel, 1)

            elif (dif > 0.5):
                if (self.vel_prefe > 80/3.6 and self.vel < 90/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel, 0.2)
                elif (self.vel_prefe > 80/3.6 and self.vel > 90/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel-3, 0.5)
                elif (self.vel_prefe < 80/3.6 and self.vel > 80/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel-3.5, 0.5)
                elif (self.vel_prefe < 80/3.6 and self.vel < 80/3.6):
                    val_aceleracion = random.normalvariate(self.media_acel-1.5, 0.3)
                
            else: # distancia por debajo de lo recomendado                 
                # se distrajo?...
                azar = random.randint(0, 1)
                if azar < self.distraido:
                    #si
                    val_aceleracion = 0 
                else:
                    #no
                    val_aceleracion = random.normalvariate(-3, 1) # no depende de si suele acelerar, va a frenar por seguridad

            if(self.vel > 80/3.6):   
                # hay camaras 
                if int(self.pos) in range(5300, 5510) or int(self.pos) in range(10300, 10510):
                    # azar = random.randint(0, 1)
                    # if azar > self.distraido:
                    # no se distrajo
                    val_aceleracion = random.normalvariate(-2,2)
                    # else:
                    #     val_aceleracion = 0
                    

            self.acel = val_aceleracion
            self.vel = self.vel + self.acel 

            if self.vel < 0:
                self.vel = 0

            
            

class Carril:
    def __init__(self, autos:list[Auto]):
        self.autos = autos
        

    def adelante(self, i):
        # i es el id del de adelante
        if self.autos[i].fin == 1:
            # el de adelante ya salio
            return 20000
        pos = self.autos[i].pos
        vel = self.autos[i].vel
        # devuelve los valores del de adelante
        return (pos, vel)
    
    # def atras(self, i):
    #     if i == len(self.autos)-1:
    #         # es el ultimo que entro
    #         return (-1000, -100000)
    #     pos_ant = self.autos[i].pos_ant
    #     pos = self.autos[i].pos
    #     # devuelve los valores del de atras
    #     return (pos_ant, pos)
    
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
    def __init__(self, id:int, p:int, t:int, v:int, a:int, p_ant):
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
        self.vel_prefe *= 1

        #randomizamos la personalidad (proba de que acelere o se mantenga)
        rand1 = random.randint(0, 5)
        if rand1 == 1:
            self.media_acel = 0.3 #lento
        elif rand1 == 2:
            self.media_acel = 1 #rapido
        else: 
            self.media_acel = 0.5 #promedio
        #self.media_acel *= 60

        # distraccion
        rand2 = random.randint(0, 5)
        if rand2 == 1 or rand2 == 2:
            self.distraido = 0.6
        else: 
            self.distraido = 0 #promedio
        
        

    def __repr__ (self):
        return str(self.__dict__)
    

    def final_recorrido(self):
        self.fin = 1
    

    def acelerar(self, pos_adel, vel_adel, time_scale):
        '''un auto puede acelerar entre -4 y 2'''

        distancia = pos_adel - self.pos
        val_aceleracion = 0
        
        # dif < 0 : me estoy acercando
        # dif > 0 : me estoy alejando
        if (self.vel == 0):
            if (distancia < 70):
                self.vel = 0
            else: 
                self.vel =  20/3.6*time_scale  #avanzo poco 
        
        else: 
            dif = distancia / self.vel 

            if(distancia > 200):
                # esta lejos
                if (self.vel < 80/3.6*time_scale):
                    val_aceleracion = random.normalvariate(self.media_acel+0.7, 0.3)
                else:
                    val_aceleracion = random.normalvariate(self.media_acel-0.8, 0.4)

            elif(distancia > 100): # distancia por encima de lo recomendado
                if (self.vel < 80/3.6*time_scale):
                    val_aceleracion = random.normalvariate(self.media_acel+0.4, 0.1)
                else:
                    val_aceleracion = random.normalvariate(self.media_acel-1, 0.1)

            elif (distancia > 80):
                if (self.vel < vel_adel):
                    val_aceleracion = random.normalvariate(self.media_acel-0.5, 0.1)
                else:
                    val_aceleracion = random.normalvariate(self.media_acel-2, 0.1)
            
            elif (distancia > 40):
                if (self.vel < vel_adel):
                    val_aceleracion = random.normalvariate(self.media_acel-0.8, 0.1)
                else:
                    val_aceleracion = random.normalvariate(self.media_acel-3.3, 0.1)

                
            else: # distancia por debajo de lo recomendado                 
                # se distrajo?...
                azar = random.randint(0, 1)
                if azar <= self.distraido:
                #     #si
                    val_aceleracion = 0 
                else:
                #     #no
                    val_aceleracion = random.normalvariate(-3.7, 0.05) # no depende de si suele acelerar, va a frenar por seguridad

            if(self.vel > 75/3.6*time_scale):   
                # hay camaras 
                if int(self.pos) in range(5400, 5510) or int(self.pos) in range(10400, 10510):
                    # azar = random.randint(0, 1)
                    # if azar > self.distraido:
                    # # no se distrajo
                    #     val_aceleracion = random.normalvariate(-2.5,0.7)
                    # else:
                    #      val_aceleracion = 0
                    val_aceleracion = random.normalvariate(-2.7,0.3)

            self.acel = val_aceleracion * time_scale
            self.vel = self.vel + self.acel 

            if self.vel < 0:
                self.vel = 0

            
            

class Carril:
    def __init__(self, autos:list[Auto]):
        self.autos = autos
        self.multas = {} # por cada hora la cantidad de multas que hubo
        self.tiempos = {} # cuanto tardaron los autos en promedio en c/ hora
        self.choques =  {} # por cada hora la cantidad de choques que hubo
        self.velocidades = {} # por cada hora la velocidad promedio
        # si es que hay diferencias...
        #self.velocidades_rapidos = {} # por cada hora la velocidad promedio de los rapidos
        #self.velocidades_lentos = {} # por cada hora la velocidad promedio de los lentos
        self.cant_autos = {} # cantidad de autos que ingresan por hora     
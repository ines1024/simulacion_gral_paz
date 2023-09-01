# Atributos: 
# ID: número identificador de auto (3 dígitos numéricos)
# {pos, temp} → posición p en tiempo t, metros
# {vel, temp} → velocidad v en tiempo t, metros/segundo
# {acel, temp} → aceleración a en tiempo t, metros/segundo
# {vel_ad, temp} → velocidad auto de adelante en tiempo t
# {vel_at, temp} → velocidad auto de atrás en tiempo t


class Auto:
    def __init__(self, id:int, p:int, t:int, v:int, a:int):
        self.id = id
        self.pos = (p, t)
        self.t = t
        self.vel = (v, t)
        self.acel = (a, t)
        self.fin = 0
        # guardar tiempo de entrada? porque el de salida se guarda en el main

    def __repr__ (self):
        return str(self.__dict__)
    
    def final_recorrido(self):
        self.fin = 1
    
    def acelerar(self):
        
        if(self.auto_ad[1] - self.pos[0] >= 30):
            val_aceleracion = 1 #numero random c mas prob de q sea alto
        
        else:
            val_aceleracion =  0 #numero random c prob mas chica
        
        self.acel = (val_aceleracion, self.t +1)
        self.vel = (self.vel[0] + self.acel[0], self.t + 1)
        self.pos = (self.pos[0] + self.vel[0], self.t + 1)
        
class Carril:
    def __init__(self, autos:list[Auto]):
        self.autos = autos
        
    def adelante(self, i):
        if self.autos[i-1].fin == 1:
            # el de adelante ya salio
            return (1000, 100000)
        v = self.autos[i-1].vel
        p = self.autos[i-1].pos
        return (v, p)
    
    def atras(self, i):
        if i == len(self.autos)-1:
            # es el ultimo que entro
            return (-1000, -100000)
        v = self.autos[i+1].vel
        p = self.autos[i+1].pos
        return (v, p)
    
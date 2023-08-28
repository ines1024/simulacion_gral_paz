# Atributos: 
# ID: número identificador de auto (3 dígitos numéricos)
# {pos, temp} → posición p en tiempo t, metros
# {vel, temp} → velocidad v en tiempo t, metros/segundo
# {acel, temp} → aceleración a en tiempo t, metros/segundo
# {vel_ad, temp} → velocidad auto de adelante en tiempo t
# {vel_at, temp} → velocidad auto de atrás en tiempo t


class Auto:
    def __init__(self, id:int, p:int, t:int, v:int, a:int, v_ad:int, v_at:int, p_ad:int, p_at:int):
        self.id = id
        self.pos = (p, t)
        self.vel = (v, t)
        self.acel = (a, t)
        self.auto_ad = (v_ad, p_ad)
        self.auto_at = (v_at, p_at)
        self.t = t
    
    def acelerar(self):
        
        if(self.auto_ad[1] - self.pos[0] >= 30):
            val_aceleracion = 1 #numero random c mas prob de q sea alto
        
        else:
            val_aceleracion =  0 #numero rand c prob mas chica
        
        self.acel = (val_aceleracion, self.t +1)
        self.vel = (self.vel[0] + self.acel[0], self.t + 1)
        self.pos = (self.pos[0] + self.vel[0], self.t + 1)

        self.t += 1
        
class Carril:
    def __init__(self, autos:list[Auto]):
        
        self.autos = autos


        
        






#Lançamento Oblíquo
import matplotlib.pyplot as plt
import numpy as np
import math


#Posições iniciais, velocidade inicial e massa
(x,y) = (0,0) m
(vx,vy) = (10,10) m/s
massa = 1.0 kg
#Força da gravidade
(fx,fy)= (0,-9.81)  m/s²
#Intervalo de tempo
dt = 0.1 s

def__init__(self, x, y, vx, vy, massa): # construtor da classe que inicializa os atributos da partícula.
    self.x = x
    self.y = y
    self.vx = vx
    self.vy = vy
    self.massa = massa
    self.tempo = 0.0 # tempo inicial

def newton(self, fx, fy, dt): # aplica a segunda lei de Newton para atualizar a velocidade e a posição da partícula com base nas forças (fx, fy) aplicadas e no intervalo de tempo dt.
    # Atualiza a velocidade
    self.vx += (fx / self.massa) * dt
    self.vy += (fy / self.massa) * dt

    # Atualiza a posição
    self.x += self.vx * dt
    self.y += self.vy * dt

    # Atualiza o tempo
    self.tempo = dt
    # Guarda os dados
    xs.append(x)
    ys.append(y)
    vxs.append(vx)
    vys.append(vy)
    ts.append(t)

    # Plotagem da trajetória
plt.figure(figsize=(8, 5))
plt.plot(xs, ys)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trajetória da Partícula (x vs y)')
plt.grid(True)
plt.show()
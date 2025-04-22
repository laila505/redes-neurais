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

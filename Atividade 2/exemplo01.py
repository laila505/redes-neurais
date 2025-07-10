#Lançamento oblíquo

#Atividade 2

import matplotlib.pyplot as plt
from particula import Particula

# Parâmetros iniciais
p = Particula(x=0, y=0, vx=10, vy=10, massa=1)
fx = 0
fy = -9.8
dt = 0.1

# Listas para armazenar posições
xs, ys = [], []

# Simulação
for _ in range(100):
    xs.append(p.x)
    ys.append(p.y)
    p.mover(fx, fy, dt)

# Gráfico
plt.plot(xs, ys)
plt.title("Trajetória da Partícula (Lançamento Oblíquo)")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid(True)
plt.savefig("grafico.png")
plt.show()

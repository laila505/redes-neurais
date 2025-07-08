#Lançamento oblíquo

#Atividade 2

import matplotlib.pyplot as plt

class Particula:
    def __init__(self, x, y, vx, vy, m):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m
        self.t = 0.0

        # Histórico
        self.x_list = [x]
        self.y_list = [y]
        self.vx_list = [vx]
        self.vy_list = [vy]
        self.t_list = [0.0]

    def aplicar_forca_gravidade(self, dt, g=-9.8):
        # Atualiza velocidade
        self.vy += g * dt

    def atualizar_posicao(self, dt):
        # Atualiza posição
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.t += dt

        # Salva no histórico
        self.x_list.append(self.x)
        self.y_list.append(self.y)
        self.vx_list.append(self.vx)
        self.vy_list.append(self.vy)
        self.t_list.append(self.t)

    def simulacao(self, dt):
        while self.y >= 0:
            self.aplicar_forca_gravidade(dt)
            self.atualizar_posicao(dt)

    def plotar_trajetoria(self):
        plt.figure(figsize=(8, 6))
        plt.plot(self.x_list, self.y_list, marker='o')
        plt.title('Trajetória da Partícula')
        plt.xlabel('Posição x (m)')
        plt.ylabel('Posição y (m)')
        plt.grid(True)
        plt.show()

# --- Programa principal ---

# Criar a partícula
particula = Particula(x=0, y=0, vx=10, vy=10, m=1)

# Rodar a simulação
particula.simulacao(dt=0.1)

# Plotar a trajetória
particula.plotar_trajetoria()

# Salva o gráfico
plt.savefig("grafico.png")
class Particula:
    def __init__(self, x, y, vx, vy, massa):
        """
        Inicializa a partícula com posição (x, y), velocidade (vx, vy) e massa.
        """
        self.x = x  # coordenada x da partícula
        self.y = y  # coordenada y da partícula
        self.vx = vx  # velocidade na direção x
        self.vy = vy  # velocidade na direção y
        self.massa = massa  # massa da partícula

    def mover(self, fx, fy, dt):
        """
        Atualiza a posição e a velocidade da partícula com base na força (fx, fy) e no intervalo de tempo dt.
        """
        ax = fx / self.massa
        ay = fy / self.massa
        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

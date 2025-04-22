#atributos da partícula 

x: coordenada x da partícula
y: coordenada y da partícula
vx: velocidade na direção x
vy: velocidade na direção y
massa: massa da partícula

__init__(self, x, y, vx, vy, massa): construtor da classe que inicializa os atributos da partícula.
newton(self, fx, fy, dt): aplica a segunda lei de Newton para atualizar a velocidade e a posição da partícula com base nas forças (fx, fy) aplicadas e no intervalo de tempo dt.
Considerar que a força é constante durante o intervalo de tempo dt.
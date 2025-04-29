#particula 
x; coordenada x da partícula
y; coordenada y da partícula
vx; velocidade na direção x
vy; velocidade na direção y
m; massa da partícula
t; tempo

#métodos
 __init__(self, x, y, vx, vy, m): construtor da classe que inicializa os atributos da partícula
newton(self, fx,fy,dt): aplica a segunda lei de newton  para atualizar a velocidade e a posição da partícula
atualiza(self, dt): atualiza a posição da partícula com base na velocidade atual e no tempo decorrido
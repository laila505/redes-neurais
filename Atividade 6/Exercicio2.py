#Exercicio 2 - Caso 1D com V(x)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from numpy.linalg import eigh

# Parâmetros iniciais

N = 5                        # Número de planos de ondas
a = 1.0                      # Período do potencial
G_vals = 2 * np.pi * (np.arange(N) - N//2) / a  # Vetor G
gamma = 50                  # Estreitamento da gaussiana

# Potencial periódico V(x)

def V(x):
    return np.exp(-gamma * (x - 0.5)**2)  # Gaussiana centrada em x=0.5


# Gráfico do potencial V(x)

x_vals = np.linspace(0, 1, 200)
V_vals = V(x_vals)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, V_vals, label='V(x)', color='darkgreen')
plt.title('Potencial periódico $V(x)$')
plt.xlabel('$x$')
plt.ylabel('$V(x)$')
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_potencial_vx.png")  # Salva gráfico
plt.close()

# ---------------------------
# Matriz V_mn (potencial no espaço recíproco)
# ---------------------------
V_mat = np.zeros((N, N), dtype=complex)

for m in range(N):
    for n in range(N):
        integrando = lambda x: V(x) * np.exp(-2j * np.pi * (G_vals[m] - G_vals[n]) * x)
        V_mat[m, n], _ = quad(integrando, 0, 1)

# Exibe matriz aproximada
print("Matriz de potencial V_mn (parte real, arredondada):")
print(np.round(V_mat.real, 4))

# ---------------------------
# Diagonalização do Hamiltoniano completo H = T + V
# ---------------------------
H = np.zeros((N, N), dtype=complex)

for m in range(N):
    for n in range(N):
        if m == n:
            H[m, n] = G_vals[m]**2 + V_mat[m, m]
        else:
            H[m, n] = V_mat[m, n]

# Diagonaliza o Hamiltoniano
autovalores, _ = eigh(H)

# ---------------------------
# Gráfico de bandas (valores próprios)
# ---------------------------
# Para comparação visual, a banda é uma linha horizontal já que H não depende de k aqui
plt.figure(figsize=(6, 4))
for i in range(len(autovalores)):
    plt.hlines(autovalores[i].real, 0, 1, label=f"Banda {i+1}")

plt.title("Bandas de energia para V(x) periódico (caso fixo)")
plt.xlabel("posição fictícia (para visualização)")
plt.ylabel("Energia")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("bandas_1D_potencial_periodico.png")  # Salva gráfico
plt.close()

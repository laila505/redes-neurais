#Exercicio 2 - Caso 1D com V(x)

import numpy as np
import matplotlib.pyplot as plt

# Número de planos de ondas considerados
N = 5  # Aumentar N melhora a precisão
G_vals = np.array([2 * np.pi * (i - N/2) / 1 for i in range(N)])  # a = 1

# Parâmetros do potencial periódico (exemplo: gaussiana estreita)
gamma = 50  # controle de alargamento (quanto maior, mais estreita)

# Definindo o potencial V(x)
def V(x):
    return np.exp(-gamma * (x - 0.5)**2)

# Gráfico de V(x) para verificar se está contido no intervalo [0,1]
x_vals = np.linspace(0, 1, 200)
V_vals = V(x_vals)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, V_vals)
plt.title("Potencial V(x)")
plt.xlabel("x")
plt.ylabel("V(x)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Cálculo dos elementos da matriz de potencial V_{mn}
V_mat = np.zeros((N, N), dtype=complex)

for m in range(N):
    for n in range(N):
        integrand = lambda x: V(x) * np.exp(-1j * (G_vals[m] - G_vals[n]) * x)
        V_mat[m, n] = np.trapz(integrand(x_vals), x_vals)

# Exibindo a matriz de potencial
print("Matriz de potencial V_mn:")
print(np.round(V_mat.real, 4))  # mostra apenas a parte real, arredondada

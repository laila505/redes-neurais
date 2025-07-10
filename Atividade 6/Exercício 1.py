#Caso 1D simples

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvalsh
from scipy.integrate import quad

# -------------------------
# Exercicio 1 - Caso 1D Simples
# -------------------------

a = 1.0       # Constante de rede do cristal
alpha = 0.5   # Termo de acoplamento entre os planos de ondas

num_k = 200
k_vals = np.linspace(-np.pi/a, np.pi/a, num_k)
bandas = []

for k in k_vals:
    k2 = k + 2 * np.pi / a
    k1 = k
    k0 = k - 2 * np.pi / a

    H = np.array([
        [k2**2, alpha, 0],
        [alpha, k1**2, alpha],
        [0, alpha, k0**2]
    ])

    energias = eigvalsh(H)
    bandas.append(energias)

bandas = np.array(bandas)

plt.figure(figsize=(8,6))
for i in range(3):
    plt.plot(k_vals, bandas[:, i], color='purple')

plt.axvline(x=-np.pi/a, color='gray', linestyle='--')
plt.axvline(x=np.pi/a, color='gray', linestyle='--')
plt.xlabel("k")
plt.ylabel("Energia")
plt.title("Diagrama de Bandas 1D - Caso Simples (Estilo Ashcroft & Mermin)")
plt.grid(True)
plt.show()

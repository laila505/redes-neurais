# Caso 1D simples

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigh

# Diagrama de Bandas 1D - Caso Simples (Estilo Ashcroft & Mermin)

a = 1.0      # Constante de rede do cristal
alpha = 0.5  # Termo de acoplamento entre planos de ondas
num_k = 200  # Número de pontos na malha de k

# Vetores k no intervalo da 1ª zona de Brillouin
k_vals = np.linspace(-np.pi/a, np.pi/a, num_k)
bandas = []

# Loop sobre k para construir e diagonalizar H(k)
for k in k_vals:
    k2 = k + 2 * np.pi / a
    k1 = k
    k0 = k - 2 * np.pi / a

    # Hamiltoniano tridiagonal 3x3
    H = np.array([
        [k2**2, alpha, 0],
        [alpha, k1**2, alpha],
        [0, alpha, k0**2]
    ])

    # Autovalores (energias)
    energias = eigh(H, eigvals_only=True)
    bandas.append(energias)

# Convertendo lista para array
bandas = np.array(bandas)

# Plotando gráfico
plt.figure(figsize=(8, 6))
for i in range(bandas.shape[1]):
    plt.plot(k_vals, bandas[:, i], color='purple')

# Linhas verticais nos limites da zona de Brillouin
plt.axvline(x=-np.pi/a, color='gray', linestyle='--')
plt.axvline(x=np.pi/a, color='gray', linestyle='--')

plt.xlabel("k")
plt.ylabel("Energia")
plt.title("Diagrama de Bandas 1D - Caso Simples (Ashcroft & Mermin)")
plt.grid(True)

# Salvar imagem
plt.tight_layout()
plt.savefig("bandas_1D.png", dpi=300)  # ← salva imagem na pasta do projeto
plt.show()

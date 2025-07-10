Exercício 2 - Caso 1D com V(x)

# Número de planos de ondas considerados
N = 5  # Aumentar N melhora a precisão
G_vals = np.array([2 * np.pi * (i - N//2) / a for i in range(N)])

# Potencial periódico - exemplo: Gaussiana estreita
gamma = 50  # Controle do alargamento (quanto maior, mais estreita)

def V(x):
    return np.exp(-gamma * (x - 0.5)**2)

# Gráfico de V(x) para verificar se está contido em [0,1]
x_vals = np.linspace(0, 1, 200)
plt.figure(figsize=(6,4))
plt.plot(x_vals, V(x_vals))
plt.title("Potencial V(x)")
plt.xlabel("x")
plt.ylabel("V(x)")
plt.grid(True)
plt.show()

# Cálculo dos elementos da matriz de potencial V_{m,n}
V_mat = np.zeros((N, N), dtype=complex)

for m, G in enumerate(G_vals):
    for n, Gp in enumerate(G_vals):
        integrando = lambda x: V(x) * np.exp(-1j * 2 * np.pi * (m - n) * x)
        resultado, _ = quad(integrando, 0, 1)
        V_mat[m, n] = resultado

print("Matriz de potencial V_{m,n}:")
print(np.round(V_mat.real, 4))

# Cálculo das bandas de energia variando k
num_k = 200
k_vals = np.linspace(-np.pi, np.pi, num_k)
bandas = []

for k in k_vals:
    H = np.zeros((N, N), dtype=complex)
    for m, G in enumerate(G_vals):
        for n, Gp in enumerate(G_vals):
            if m == n:
                H[m, n] = (k + G)**2
            H[m, n] += V_mat[m, n]

    energias = eigvalsh(H)
    bandas.append(energias)

bandas = np.array(bandas)

# Plot das bandas
plt.figure(figsize=(8,6))
for i in range(N):
    plt.plot(k_vals, bandas[:, i], color='blue')

plt.axvline(x=-np.pi, color='gray', linestyle='--')
plt.axvline(x=np.pi, color='gray', linestyle='--')
plt.xlabel("k")
plt.ylabel("Energia")
plt.title("Diagrama de Bandas - Potencial Arbitrário (Gaussiana)")
plt.grid(True)
plt.show()
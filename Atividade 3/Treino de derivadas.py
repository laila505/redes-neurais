#Atividade 3_Derivadas

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)

def generate_data(nx, qtde):
    x = np.linspace(-1, 1, nx).reshape(-1, 1)
    y = []
    dy = []

    for _ in range(qtde):
        # Escolhe aleatoriamente grau 3 ou 4
        grau = np.random.choice([3, 4])

        # Gera raízes simétricas
        if grau == 3:
            r = np.random.uniform(0.1, 2.0)
            roots = [-r, 0, r]
        else:
            r1, r2 = np.random.uniform(0.1, 2.0, 2)
            roots = [-r1, r1, -r2, r2]

        # Coeficientes do polinômio a partir das raízes
        coeffs = np.poly(roots)

        # Avaliação da função e derivada
        polinomio = np.polyval(coeffs, x)
        derivada = np.polyval(np.polyder(coeffs), x)

        # Normalização e ruído
        norm_factor = np.max(np.abs(polinomio))
        noise_y = 0.1 * np.random.randn(len(x)).reshape(-1, 1)
        noise_dy = 0.1 * np.random.randn(len(x)).reshape(-1, 1)

        y.append(polinomio / norm_factor + noise_y)
        dy.append(derivada / norm_factor + noise_dy)

    y = np.hstack(y).T
    dy = np.hstack(dy).T
    return y, dy, x

# Geração dos dados
y, dy, x = generate_data(50, 10000)

# Separação em treino/teste
X_train, X_test, y_train, y_test = train_test_split(y, dy, test_size=0.2, random_state=42)

# Modelo MLP
neurons = 10
layers = 10
model = MLPRegressor(
    hidden_layer_sizes=tuple([neurons] * layers),
    activation='tanh',
    solver='adam',
    max_iter=100000,
    random_state=42,
    learning_rate='adaptive',
    learning_rate_init=0.001,
    n_iter_no_change=50,
    tol=1e-8,
    verbose=True
)

# Treinamento
model.fit(X_train, y_train)

# Avaliação
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.6f}")

# Plotar algumas comparações entre derivadas reais e previstas
num_samples_to_plot = 3
indices = np.random.choice(len(X_test), num_samples_to_plot, replace=False)

plt.figure(figsize=(12, 6))
for i, idx in enumerate(indices):
    plt.subplot(1, num_samples_to_plot, i+1)
    plt.plot(x, y_test[idx], label='Derivada Real', color='orange')
    plt.plot(x, y_pred[idx], label='Derivada Prevista', color='blue', linestyle='--')
    plt.title(f"Amostra {idx}")
    plt.grid(True)
    if i == 0:
        plt.ylabel("dy")
    plt.xlabel("x")
    plt.legend()

plt.suptitle("Comparação entre derivadas reais e previstas (MLP)")
plt.tight_layout()
plt.show()


#Atividade 3_primeira parte: fitar o seno
#Codigo modificado para via Pytorch

import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import mean_squared_error

# 1. Gerar dados de treino
np.random.seed(42)
torch.manual_seed(42)

num_samples = 100
angles_train = np.random.uniform(0, 4 * np.pi, num_samples).reshape(-1, 1)
sin_values_train = np.sin(angles_train)

# Adicionar ruído
noise = np.random.normal(0, 0.1, sin_values_train.shape)
sin_values_train += noise

# Converter para tensores do PyTorch
X_train = torch.tensor(angles_train, dtype=torch.float32)
y_train = torch.tensor(sin_values_train, dtype=torch.float32)

# 2. Definir modelo FCNN
class FCNN(nn.Module):
    def __init__(self):
        super(FCNN, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(1, 10),
            nn.Tanh(),
            nn.Linear(10, 10),
            nn.Tanh(),
            nn.Linear(10, 10),
            nn.Tanh(),
            nn.Linear(10, 1)
        )

    def forward(self, x):
        return self.model(x)

model = FCNN()

# 3. Definir função de perda e otimizador
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 4. Treinar o modelo
epochs = 1000
losses = []
patience = 50
best_loss = float('inf')
counter = 0

for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    loss.backward()
    optimizer.step()
    losses.append(loss.item())

    # Early stopping manual
    if loss.item() < best_loss - 1e-6:
        best_loss = loss.item()
        counter = 0
        best_model_state = model.state_dict()
    else:
        counter += 1
        if counter >= patience:
            print(f"Early stopping at epoch {epoch}")
            break

# Restaurar melhor modelo
model.load_state_dict(best_model_state)

# 5. Visualizar curva de perda
plt.figure(figsize=(8, 4))
plt.plot(losses)
plt.title("Curva de Perda (Loss) durante o Treinamento")
plt.xlabel("Época")
plt.ylabel("Loss (MSE)")
plt.grid(True)
plt.tight_layout()
plt.show()

# 6. Dados de teste
num_test_samples = 50
angles_test = np.linspace(0, 6 * np.pi, num_test_samples).reshape(-1, 1)
sin_values_true = np.sin(angles_test)

X_test = torch.tensor(angles_test, dtype=torch.float32)

# 7. Fazer previsões
model.eval()
with torch.no_grad():
    y_pred = model(X_test).numpy()

# 8. Avaliar o modelo
mse = mean_squared_error(sin_values_true, y_pred)
print(f"Mean Squared Error on Test Data: {mse}")

# 9. Visualizar os resultados
plt.figure(figsize=(10, 6))
plt.scatter(angles_train, sin_values_train, label='Training Data', alpha=0.5)
plt.plot(angles_test, sin_values_true, label='True sin(theta)', color='blue')
plt.plot(angles_test, y_pred, label='Predicted sin(theta)', color='red')
plt.xlabel('Angle (radians)')
plt.ylabel('sin(theta)')
plt.title('FCNN Interpolation of sin(theta) using PyTorch')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 10. Salvar o modelo treinado
torch.save(model.state_dict(), "modelo_seno_pytorch.pth")
print("Modelo salvo como 'modelo_seno_pytorch.pth'")

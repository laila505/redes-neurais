# 📚 Atividade 4 — Physics Informed Neural Networks (PINNs)

# Resfriamento de uma Caneca de Café com Redes Neurais e PINNs ☕️

Este projeto resolve a equação diferencial do resfriamento de uma caneca de café usando diferentes métodos:

- Solução Analítica  
- Método de Runge-Kutta de 4ª ordem (RK4)  
- Rede Neural de Regressão Simples  
- PINN (Physics-Informed Neural Network)  

---

## 🔧 Equação Modelada

A equação diferencial ordinária (EDO) do resfriamento é:

$$
\frac{dT}{dt} = r (T_{amb} - T)
$$


Onde:

- **T** = temperatura do café  
- **T<sub>amb</sub>** = 25 °C (temperatura ambiente)  
- **r** = 0.005 s⁻¹ (taxa de resfriamento)
  

---

## 📌 Etapas

1. ✅ Solução **analítica** da EDO.  
2. ✅ Solução **numérica** com RK4.  
3. ✅ Geração de dados **sintéticos** com ruído.  
4. ✅ Ajuste com Rede Neural de **Regressão Simples**.  
5. ✅ Treinamento de **PINN** com conhecimento da equação.  
6. ✅ Comparação dos resultados obtidos.  

---

## Gráficos
Comparação: Solução Analítica vs PINN + Dados Sintéticos

![Gráfico de Comparação](./grafico_comparacao.png)

---


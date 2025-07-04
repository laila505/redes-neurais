Nesta pasta serão apresentados alguns exercícios voltados para o entendimento básico do funcionamento das Redes Neurais. Neste contexto a implementação e estudo de **Physics Informed Neural Networks (PINNs)**, abordando a resolução de equações diferenciais ordinárias (EDOs) com restrições físicas.  
As PINNs combinam:
1. **Dados observados (experimentais ou simulados)** com
2. **Restrição física (equação diferencial governante)**

Isso permite resolver EDOs ou EDPs incorporando conhecimento físico, mesmo com poucos dados. Aqui, foi resolvida a EDO do resfriamento de uma caneca de café, definida por:

\[
\frac{dT}{dt} = -k (T - T_a)
\]

onde:
- \( T \) é a temperatura do café,
- \( T_a = 25°C \) é a temperatura ambiente,
- \( k = 0.005 \) 1/s é a taxa de resfriamento.
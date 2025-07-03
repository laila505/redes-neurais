
# 📚 Gradiente Descendente 

Nesta atividade há exercícios práticos para implementação e análise do algoritmo de **Gradiente Descendente**, ao qual se verifica a taxa de aprendizado, posição inicial e a presença de múltiplos mínimos.


---

No exercício 1, faz se uma análise dos parâmetros de um gradiente mais simples. Neste sentido, o exercício busca 
visualizar a função e a trajetória da partícula.  Além de explorar o efeito de diferentes taxas de aprendizado e posições iniciais.  

No exercício 2, o processo de resolução foi o mesmo para uma nova função.Esta função tem dois mínimos globais, com isso. estudou-se o comportamento do algoritmo em função com múltiplos mínimos globais e também testou-se como a posição inicial e a taxa de aprendizado afetam o resultado.  

No exercício 3, buscou-se investigar como a adição de um termo linear  altera a altura dos mínimos da função.
Também foi observado a convergência do algoritmo variando a taxa de aprendizado , 𝛼. Se o valor de 
muito pequeno, o algoritmo avança devagar e pode demorar muito para convergir.em contrapartida, caso seja muito grande, o algoritmo pode divergir, ou seja, os valores ficam cada vez maiores ou oscilam sem parar, o que causa erros como o overflow.

No exercício 4, fo feito a minimização da função: `U(x, y) = (sin(x)cos(y) + 2(xy)²) / 1000` , ao qual foi Visualizado a função com gráfico de contorno, o desenho da trajetória da partícula no plano 2D e monitorando o valor da função ao longo das iterações e explorar o impacto da taxa de aprendizado e posição inicial.  Este exercício teve duas ´partes:

a) Gerar gráfico de contorno da função  com a trajetória da partícula.

b) Plotar a evolução do valor de  ao longo das iterações (gráfico  vs. , chamado de gráfico de epochs).
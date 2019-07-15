# Projeto 2VA - Aprendizagem de Máquina				
## UFRPE - BCC - IA

## Equipe:
- Marcos Antonio da silva
- Elias Jose
- Irismar Neris

## Tema: 
- Reconhecimento de caracteres
- Problema Classificação de dados

## Descrição:				
Este projeto consiste em utilizar algoritmo de aprendizagem de maquina para resolver o problema de reconhecimento de caracteres com a classificação de dados e depois classificar imagens de números manuscritos.

### 1. INTRODUÇÂO

Este projeto se trata da execução de um algoritmo para treinamento e depois classificar imagens de números manuscritos, utilizando uma base de dados. A fim de tratar esse problema, foi escolhido o algoritmo K-Nearest Neighbor (KNN), arvore de decisão, naive bayes para poder obter um melhor resultado verificando qual a taxa de erro menor dos algoritmos escolhidos, também utilizaremos as distancias Euclidiana, Manhattan, para saber as distancias entre os determinados pontos. Fazendo assim uma comparação de resultados entre os tres algoritmos assim sendo verificando o mas útil em classificação de objetos, utilizaremos a linguagem python e o framework weka.

### 2. MATERIAIS
 Classificar uma base de dados, que contém imagens de caracteres de 0 até 9.  
 ● As imagens são de tamanho 28x28 pixels  
 ● Imagens em tons de preto  
 ● Imagens binárias (preto e branco)  


### 3. MÉTODOS
Descrever o algoritmo a ser utilizado. 
Apresentar as diferentes parametrizações a serem consideradas
Foi utilizada uma base de dados do The MNIST database of handwritten digits.  
 ● A base de dados foi dividida em ⅔ para treinamento e ⅓ para teste  
 ● A conversão das imagens foi feita usando um programa escrito em Python e  salva como um vetor de 784 posições.  
 ● Notepad++ foi utilizado para facilitar a rotular cada linha com a sua classe  especificada.  4. Implementação dos algoritmos  4.1. 

### 4. EXPERIMENTOS E RESULTADOS
Apresentação dos resultados obtidos
- Tabela com os valores da medida de avaliação considerada (ex. taxa de acerto, etc)
- Gráfico comparando os melhores resultados de cada método considerado




### 5. CONCLUSÃO
Podemos verificar que o algoritmo KNN é bom algoritmo para classificação de objetos,  devido à sua simples implementação e uma taxa de acerto relativamente alta, porém um  alto custo computacional é exigido, pois o algoritmo guarda na memória todo conjunto  de treinamento. As 3 métricas utilizadas, a que teve a menor acurácia foi a distância de  Manhattan, devido que é uma simplificação da distância Euclidiana, porém devido à sua  simplicidade, teve o melhor desempenho. A que teve a melhor acurácia foi a distância  de Bray-Curis, juntamente com um desempenho satisfatório. Distância Euclidiana  obteve uma taxa de acertos alta, porém com o pior desempenho entre as três métricas,  devido que esta métrica precisa realizar mais cálculos matemáticos que as outras duas.   





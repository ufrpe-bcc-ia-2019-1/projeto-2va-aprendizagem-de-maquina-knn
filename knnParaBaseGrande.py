#-*- coding: utf-8 -*-
import csv
import random
import math
import operator


def carregarBancoDeDados(nomeArquivo, dividir, conjuntoTreino=[], conjuntoTeste=[]):	#Esta funação vai carregar o banco de dados
    with open(nomeArquivo, 'rb') as csvfile:	#Também vai dividir aleatoriamente a base de dados em conjunto de treinamento e testes
        linhas = csv.reader(csvfile)
        conjuntoDeDados = list(linhas)
        for x in range(len(conjuntoDeDados) - 1):#tamanho do conjunto de dados é a quantidade de linhas
            for y in range(784):	#784 é o tamanho do vetor, pois cada pixel da imagem representa uma posição do vetor
                conjuntoDeDados[x][y] = float(conjuntoDeDados[x][y])
            if random.random() < dividir:
                conjuntoTreino.append(conjuntoDeDados[x])
            else:
                conjuntoTeste.append(conjuntoDeDados[x])

#Para fazer previsões, temos que calcular a similaridade entre quaisquer instâncias de dados. Utilizamos 3 medidas de distâncias descritas abaixo.

def distanciaEuclidiana(instancia1, instancia2, length):	#Distância Euclidiana
    distancia = 0			#A função vai calcular a similaridade entre as instâncias de dados
    for x in range(length):
        distancia += pow((instancia1[x] - instancia2[x]), 2)
    return math.sqrt(distancia)

def distanciaManhattan(instancia1, instancia2, length):	#Distância de Manhattan
    distancia = 0                                       #A função vai calcular a similaridade entre as instâncias de dados
    for x in range(length):
        distancia += abs(instancia1[x] - instancia2[x])
    return distancia

def distanciaBrayCurtis(instancia1, instancia2, length):	#Distância de Bray-Curtis
    distancia = 0                                       ##A função vai calcular a similaridade entre as instâncias de dados
    distancia2 = 0
    for x in range(length):
        distancia += abs(instancia1[x] - instancia2[x])
        distancia2 += abs(instancia1[x] + instancia2[x])
    return distancia/distancia2

#Algoritmo KNN

def obterVizinhos(conjuntoTreino, conjuntoTeste, k):#Função que retorna os k-vizinhos mais similares do conjunto de treinamento para uma determinada instância de teste
    distancias = []  #Calcula a distância para todas as instâncias e seleciona um subconjunto com os menores valores de distância
    length = len(conjuntoTeste) - 1    #Função da distância Euclidiana
    for x in range(len(conjuntoTreino)):
        dist = distanciaEuclidiana(conjuntoTeste, conjuntoTreino[x], length)
        distancias.append((conjuntoTreino[x], dist))
    distancias.sort(key=operator.itemgetter(1)) #função classifica o vetor de acordo com o primeiro elemento do vetor, na forma crescente
    vizinhos = []
    for x in range(k):
        vizinhos.append(distancias[x][0])
    return vizinhos

def obterResposta(vizinhos): #Função para classificar, baseadas nas repostas previstas. Obtém a maioria dos votos de respostas dada pelos vizinhos.
    votosClasses = {}		#Cada vizinho vota em seu atributo de classe e que possui a maior quantidade de votos é escolhido
    for x in range(len(vizinhos)):	
        resposta = vizinhos[x][-1]
        if resposta in votosClasses:
            votosClasses[resposta] += 1
        else:
            votosClasses[resposta] = 1
    votosClassificados = sorted(votosClasses.iteritems(), key=operator.itemgetter(1), reverse=True) #classifica os elementos do vetor em ordem descrescente
    return votosClassificados[0][0]

def obterPrecisao(conjuntoTeste, previsoes): #Função para medir a acurácia das previsões. Soma o total de previsões corretas e retorna a precisão em forma de porcentagem das classificações corretas
    correto = 0			#Para medir a acurácia a razão entre o total de previsões corretas sobre o total de previsões feitas
    for x in range(len(conjuntoTeste)):			
        if conjuntoTeste[x][-1] == previsoes[x]:
            correto += 1
    return (correto / float(len(conjuntoTeste))) * 100.0

def main():
    #Preparar os dados
    conjuntoTreino = []
    conjuntoTeste = []
    dividir = 0.67				#divide 33% da base de dados para teste e 67% para treino
    carregarBancoDeDados('baseGrande.csv', dividir, conjuntoTreino, conjuntoTeste)
    print ('Conjunto de treinamento: ' + repr(len(conjuntoTreino)))
    print ('Conjunto de teste: ' + repr(len(conjuntoTeste)))
    #Gerar previsões
    previsoes = []
    k = 3
    print('K = ' + repr(k))
    for x in range(len(conjuntoTeste)):
        vizinhos = obterVizinhos(conjuntoTreino, conjuntoTeste[x], k)
        resultado = obterResposta(vizinhos)
        previsoes.append(resultado)
        print('> previsto=' + repr(resultado) + ', atual=' + repr(conjuntoTeste[x][-1]))
    precisao = obterPrecisao(conjuntoTeste, previsoes)
    print('Precisao: ' + repr(precisao) + '%')
	
#k = 5
    #print('K = ' + repr(k))
    #for x in range(len(conjuntoTeste)):
        #vizinhos = obterVizinhos(conjuntoTreino, conjuntoTeste[x], k)
       # resultado = obterResposta(vizinhos)
      #  previsoes.append(resultado)
     #   print('> previsto=' + repr(resultado) + ', atual=' + repr(conjuntoTeste[x][-1]))
    #precisao = obterPrecisao(conjuntoTeste, previsoes)
    #print('Precisao: ' + repr(precisao) + '%')
	
#k = 9
 #   print('K = ' + repr(k))
  #  for x in range(len(conjuntoTeste)):
   #     vizinhos = obterVizinhos(conjuntoTreino, conjuntoTeste[x], k)
    #    resultado = obterResposta(vizinhos)
     #   previsoes.append(resultado)
      #  print('> previsto=' + repr(resultado) + ', atual=' + repr(conjuntoTeste[x][-1]))
   # precisao = obterPrecisao(conjuntoTeste, previsoes)
   # print('Precisao: ' + repr(precisao) + '%')
		
main()

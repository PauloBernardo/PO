from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
  
mpl.use('Agg')
  
def bubble(vetor):
  number_swap = 0
  for t in range(len(vetor)):
    for i in range ((len(vetor)-1)):
        if vetor[i]>vetor[i+1]:
            number_swap = number_swap + 1
            vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
  return number_swap


def desenhaGrafico(x,y, file_name, label, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = label)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)
   
tam = [10000,20000,50000,100000]
times = []
numbers_swap = []
  
for i in range(4):
    lista = geraLista(tam[i])
    times.append(timeit.timeit("bubble({})".format(lista),setup="from __main__ import bubble",number=1)) 
    numbers_swap.append(bubble(lista))

desenhaGrafico(tam,times, "GraficoTempo.png", "Tempo")
desenhaGrafico(tam, numbers_swap, "GraficoNumeroIteracoes.png", "NumeroIteracao")

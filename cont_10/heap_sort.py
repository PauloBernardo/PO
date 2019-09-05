import random
import timeit
import matplotlib.pyplot as plt

def forma_estrutura_heap(lista, final, raiz):
  maior = raiz
  direita = raiz * 2 + 2
  esquerda = raiz * 2 + 1
  
  if esquerda < final and lista[esquerda] > lista[raiz]:
    maior = esquerda
    
  if direita < final and lista[direita] > lista[maior]:
    maior = direita
    
  if maior != raiz:
    lista[maior], lista[raiz] = lista[raiz], lista[maior]
    
    forma_estrutura_heap(lista, final, maior)
    
    
def heap_sort(lista):
  tam = len(lista)
  
  for i in range(tam, -1, -1):
    forma_estrutura_heap(lista, tam, i)
    
  for i in range(tam-1, 0, -1):
    lista[i], lista[0] = lista[0], lista[i]
    forma_estrutura_heap(lista, i, 0)


def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


tam = [100000, 200000, 500000, 1000000, 2000000]
times = []
for i in range(len(tam)):
    lista_aleatoria = list(range(1, tam[i] + 1))
    random.shuffle(lista_aleatoria)
    times.append(timeit.timeit("heap_sort({})".format(lista_aleatoria),
                               setup="from __main__ import heap_sort, forma_estrutura_heap", number=1))


desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo heap_sort", xl="Tamanho da lista", yl="Tempo")

from random import randint, shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


def gera_lista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

def gera_lista_invertida(tam):
    lista = list(range(1, tam+1))
    lista.reverse()
    return lista

mpl.use('Agg')


def select_sort(vetor):
    number_comparation = 0
    for i in range(len(vetor)):
        menor_indice = i
        for j in range(i, (len(vetor))):
            number_comparation = number_comparation + 1
            if vetor[j] < vetor[menor_indice]:
                menor_indice = j

        if menor_indice != i:
            aux = vetor[menor_indice]
            vetor[menor_indice] = vetor[i]
            vetor[i] = aux
    return number_comparation


def desenhaGrafico(x,y, y2, file_name, label1, label2, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = label1)
    ax.plot(x,y2, label = label2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

tam = [10000,20000,50000,100000]
times_normal = []
times_invert = []
numbers_comparation = []
numbers_comparation_invert = []

for i in range(4):
    lista = gera_lista(tam[i])
    lista_invertida = gera_lista_invertida(tam[i])

    times_normal.append(timeit.timeit("select_sort({})".format(lista), setup="from __main__ import select_sort", number=1))
    times_invert.append(timeit.timeit("select_sort({})".format(lista_invertida), setup="from __main__ import select_sort", number=1))
    numbers_comparation.append(select_sort(lista))
    numbers_comparation_invert.append(select_sort(lista_invertida))

desenhaGrafico(tam, times_normal, times_invert, "GraficoTempo2.png", "Tempo vetor normal", "Tempo vetor invertido")
desenhaGrafico(tam, numbers_comparation, numbers_comparation_invert, "GraficoNumeroComparacoes.png", "Numero de comparações normal", "Numero de comparações invertido")

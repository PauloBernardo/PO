import random
import timeit
import matplotlib.pyplot as plt


def intercala(lista, inicio, meio, fim):
    x1 = inicio
    x2 = meio
    aux = []
    while x1 < meio and x2 < fim:
        if lista[x1] < lista[x2]:
            aux.append(lista[x1])
            x1 += 1
        else:
            aux.append(lista[x2])
            x2 += 1
    for i in range(x1, meio):
        aux.append(lista[i])
    for i in range(x2, fim):
        aux.append(lista[i])
    for i in range(len(aux)):
        lista[inicio+i] = aux[i]


def merge_sort(lista, inicio, fim):
    if inicio < fim-1:
        meio = (inicio+fim)//2
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        intercala(lista, inicio, meio, fim)


def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


tam = [100000, 200000, 400000, 500000, 1000000, 2000000]
times = []

for i in range(len(tam)):
    lista_invertida = list(range(1, tam[i]+1))
    random.shuffle(lista_invertida)
    times.append(timeit.timeit("merge_sort({}, {}, {})".format(lista_invertida, 0, len(lista_invertida)),
                               setup="from __main__ import merge_sort, intercala", number=1))


desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo merge_sort", xl="Tamanho da lista", yl="Tempo")

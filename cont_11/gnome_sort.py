import random
import timeit
import matplotlib.pyplot as plt


def gnome_sort(lista):
    tam = len(lista)
    index = 0
    while index < tam:
        if index == 0:
            index = index + 1
        if lista[index] >= lista[index - 1]:
            index = index + 1
        else:
            lista[index], lista[index - 1] = lista[index - 1], lista[index]
            index = index - 1


def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


tam = [10000,20000,50000,100000]
times = []
for i in range(len(tam)):
    lista_aleatoria = list(range(1, tam[i] + 1))
    random.shuffle(lista_aleatoria)
    times.append(timeit.timeit("gnome_sort({})".format(lista_aleatoria),
                               setup="from __main__ import gnome_sort", number=1))


desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo gnome_sort", xl="Tamanho da lista", yl="Tempo")

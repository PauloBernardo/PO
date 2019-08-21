import random
import timeit
import matplotlib.pyplot as plt


def shell_sort(lista):
    tamanho_lista = len(lista)
    intervalo = tamanho_lista // 2

    while intervalo > 0:
        for i in range(intervalo, tamanho_lista):
            aux = lista[i]
            j = i
            while j >= intervalo and lista[j - intervalo] > aux:
                lista[j] = lista[j - intervalo]
                j -= intervalo
            lista[j] = aux
        intervalo //= 2


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
    lista_aleatoria = list(range(1, tam[i] + 1))
    random.shuffle(lista_aleatoria)
    times.append(timeit.timeit("shell_sort({})".format(lista_aleatoria),
                               setup="from __main__ import shell_sort", number=1))


desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo shell_sort", xl="Tamanho da lista", yl="Tempo")

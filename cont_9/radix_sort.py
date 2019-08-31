import random
import timeit
import matplotlib.pyplot as plt

def radix_sort(lista):
    maximo = max(lista) if len(lista) > 2 else 0
    baldes = [ [] for i in range(10)]
    exp = 1
    while maximo // exp > 0:
        for i in lista:
            baldes[(i//exp)%10].append(i)
        del lista[:]
        for i in range(len(baldes)):
            lista.extend(baldes[i])
            baldes[i] = []
        exp *= 10
    return lista


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
    times.append(timeit.timeit("radix_sort({})".format(lista_aleatoria),
                               setup="from __main__ import radix_sort", number=1))


desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo radix_sort", xl="Tamanho da lista", yl="Tempo")

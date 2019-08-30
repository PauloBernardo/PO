import random
import timeit
import matplotlib.pyplot as plt

def bucket_sort(lista):
    maximo = max(lista)
    num_baldes = maximo//10
    baldes = [ [] for i in range(num_baldes)]
    for i in lista:
        for j in range(num_baldes-1, -1, -1):
            if i >= j*10:
                baldes[j].append(i)
                break

    for balde in baldes:
        counting_sort(balde)

    return [i for j in baldes for i in j]


def counting_sort(lista):
    maior = max(lista)
    aux = [0] * (maior + 1)
    for i in range(len(lista)):
        aux[lista[i]] += 1
    index = 0
    for i in range(len(aux)):
        num_repeticao = aux[i]
        for _ in range(num_repeticao):
            lista[index] = i
            index += 1


def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


tam = [10000, 20000, 50000, 100000, 200000]
times = []
for i in range(len(tam)):
    lista_aleatoria = list(range(1, tam[i] + 1))
    random.shuffle(lista_aleatoria)
    times.append(timeit.timeit("bucket_sort({})".format(lista_aleatoria),
                               setup="from __main__ import counting_sort, bucket_sort", number=1))


desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo bucket_sort", xl="Tamanho da lista", yl="Tempo")

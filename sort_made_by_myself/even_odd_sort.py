import random
import timeit
import matplotlib.pyplot as plt

def intercala(lista,lista1,lista2):
    x,y,z = (0,0,0)
    tam = len(lista1)+len(lista2)
    while x != tam:
        if len(lista1) == 0:
            lista[x] = lista2[0]
            lista2.pop(0)
        elif len(lista2) == 0:
            lista[x] = lista1[0]
            lista1.pop(0)
        elif lista1[0]<lista2[0] or len(lista2)==0:
            lista[x] = lista1[0]
            lista1.pop(0)
        else:
            lista[x] = lista2[0]
            lista2.pop(0)
        x += 1


def merge_sort(lista):
    if len(lista)>1:
        meio = len(lista)//2
        lista1 = lista[:meio]
        lista2 = lista[meio:]
        merge_sort(lista1)
        merge_sort(lista2)
        intercala(lista, lista1, lista2)


def even_odd_sort(lista):
    even_lista = []
    odd_lista = []
    for i in lista:
        if i % 2 == 0:
            even_lista.append(i)
        else:
            odd_lista.append(i)
    merge_sort(even_lista)
    merge_sort(odd_lista)
    intercala(lista, even_lista, odd_lista)


def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


tam = [1000, 2000, 4000, 5000, 10000, 20000]
times = []
for i in range(len(tam)):
    lista_aleatoria = list(range(1, tam[i] + 1))
    random.shuffle(lista_aleatoria)
    times.append(timeit.timeit("even_odd_sort({})".format(lista_aleatoria),
                               setup="from __main__ import even_odd_sort, merge_sort, intercala", number=1))


desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo even_odd_sort", xl="Tamanho da lista", yl="Tempo")

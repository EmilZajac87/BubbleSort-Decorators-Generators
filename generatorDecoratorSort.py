#learn how to use decorators(time when function was opened, sqrt another var in func), generator
#sort another method than sord or sorted (alghoritm) and operation with files

import time

def decorators1(func):

    def decorateFunction(*args, **kwargs):

        i = [x**2 for x in func(*args, **kwargs)]

        return i
    return decorateFunction

@decorators1
def NumerInRange(endOfRange):

    for i in range(1, endOfRange+1):
        yield i

def normalSort(lista):

    return sorted(lista)

def normalSortAnother(lista):
    lista.sort()
    return lista

def bubbleSort(lista):

    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i + 1] = lista[i+1], lista[i]
    return lista

lista = [54, 1, 87, 100, 23, 4, 6, 1]

lista_sorted = normalSort(lista)
print("This list was sorted by sorted: {}".format(lista_sorted))

lista_sort = normalSortAnother(lista)
print("This list was sorted by sort: {}".format(lista_sort))

lista_bubble_sort = bubbleSort(lista)
print("This list was sorted by bubble sort alghorytm {}".format(lista_bubble_sort))


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

def normalSortAnotherReverse(lista):
    lista.sort(reverse=True)
    return lista

def bubbleSort(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i + 1] = lista[i+1], lista[i]
    return lista

lista = [54, 1, 87, 100, 23, 4, 6, 1]

lista_sorted = normalSort(lista)
print("This list was sorted by sorted: {}".format(lista_sorted))

lista_sort = normalSortAnotherReverse(lista)
print("This list was sorted by sort(reverse): {}".format(lista_sort))

lista_bubble_sort = bubbleSort(lista)
print("This list was sorted by bubble sort alghorytm {}".format(lista_bubble_sort))


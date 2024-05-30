
import random

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p - 1)
        quicksort(lista, p + 1, fim)


def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

def inverte(lista):
    tamanho =len(lista)
    lista_invertida = []
    for j in range(tamanho-1,-1,-1):
        lista_invertida.append(lista[j])
    return lista_invertida

any_numbers = random.sample(range(1, 1000), 42)
print("Antes da ordenação:", any_numbers)
quicksort(any_numbers)
print("Depois da ordenação:", any_numbers)
print("toma invertida:" , inverte(any_numbers))
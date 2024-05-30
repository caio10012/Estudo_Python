def inverte(lista):
    tamanho = len(lista)
    lista_invertida = []
    for j in range(tamanho-1,-1,-1):
        lista_invertida.append(lista[j])
    return lista_invertida

lista_normal= [1,2,3]
print(lista_normal)
print(inverte(lista_normal))

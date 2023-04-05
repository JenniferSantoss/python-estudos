#Questão 01: Implementar uma solução que retorne o menor elemnto de uma lista

def encontrarMinimo(lista):
    minimo = lista[0]
    for elem in lista:
        if(elem < minimo):
            minimo = elem
    return minimo


lista_teste = [2, 10, 3, 1, 4, 5]
menor = encontrarMinimo(lista_teste)
print('O menor elemento da lista: [{}]'.format(menor))
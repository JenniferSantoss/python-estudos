# Questão 02: Considere a lista abaixo:

lista = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Implementar uma solução através de programação funcional para imprimir somente os números pares.

fEhPar = lambda x: x % 2 == 0

pares = list(filter(fEhPar, lista))

print(f'Numeros pares = {pares}')
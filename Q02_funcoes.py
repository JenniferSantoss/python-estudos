# Questão 02: Implementar uma solução em Python que retorne a soma de todos os elementos pares de uma lista

def ehPar(n):
    r = (n%2==0)
    return r

def soma_par(lst):
    soma=0
    for num in lst:
        if(num(ehPar)):
            soma = soma + num
    return soma


lista = [10, 2, 5, 7, 6, 3]
soma = soma_par(lista)
print(f'Resultado: {soma}')
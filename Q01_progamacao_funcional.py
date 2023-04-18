#Considera a lista abaixo:

veiculos = ['aviao', 'carro', 'navio', 'onibus']

#Implementar uma solução através da programação funcional para transformar todos os nomes em maisculo.

f_maiuscula = lambda x: str.upper(x)

nomes_maiusculos = list(map(f_maiuscula, veiculos))

print(f'Nomes maiusculos = {nomes_maiusculos}')
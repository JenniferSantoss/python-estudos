#Para variável string

nome = 'exemplo de string em python'
print(nome)
print('valor da variavel nome = {}'.format(nome))
print(f'valor da variavel nome = {nome}')

print(nome.upper())
print(nome.lower())
print(nome.split())

#Exemplo de Atribuição Multípla

a, b = 1, 2
print('Antes da troca')
print(f'Valor das variaveis: a = {a}, b = {b}')

#Primeira troca - Atribuição Multípla

temp = a 
a = b
b = temp
print('Primeira troca')
print(f'Valor das variaveis: a = {a}, b = {b}')

#Segunda troca - Atribuição Multípla
a,b = b,a

print('Segunda troca')
print(f'Valor das variaveis: a = {a}, b = {b}')


#Operações Numéricas
x = 10
print(f'x = {x}')
x +=2
print(f'x = {x}')
x-=2
print(f'x = {x}')
x/=2
print(f'x = {x}')
x*=2
print(f'x = {x}')
x%=2
print(f'x = {x}')

#Para saber o tipo da variável 
print(type(x))
print(type(nome))






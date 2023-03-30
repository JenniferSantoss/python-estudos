#Entrada de dados com a função Input

nome = input('Escreva seu nome: ')
print(nome)

#imc

peso = eval(input('Digite seu peso: '))
altura = eval(input('Digite sua altura: '))
imc = peso / altura**2
print('IMC = ', imc)
print('finish')

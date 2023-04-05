#Laço FOR

for item in range(2, 9, 3):
    print(item)


nome = input("Entre com seu nome: \n")
for letra in nome:
    print(letra) 


nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']
for nome in nomes:
    print(nome)    

#While    

palavra = input('Entre com uma palavra: \n ')
while palavra != 'sair':
    palavra = input('Digite sair para encerrar o laço: \n')
print('Você digitou sair e agora está fora do laço')    

#while break

while True:
    palavra = input('Entre com uma palavra: \n')
    if palavra == 'sair':
        break
print('Você digitou sair e agora está fora do laço')

#While continue

for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

#While pass

for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')
#Questão 03: Implementaar uma solução em Python, através do uso da thread, que faça:
# a) Inicie a execução de duas Thread;
# b) A primeira thread deve calcular o cubo de um numero;
# c) A segunda thread deve calcular o quadrado de um numero;
# d) Coloque a primeira e a segunda thread para esperar 3 e 2 segudndos;
# e) Informar a ordem de execucao das threads

from time import sleep
from threading import Thread

def calcular_cubo(num, tempo_espera):
    print(f'Cubo = {num * num * num}')
    sleep(tempo_espera)
    print('Conclusao da tarefa calcular cubo')

def calcular_quadrado(num, tempo_espera):
    print(f'Quadrado = {num * num}')
    sleep(tempo_espera)
    print('Conclusao da tarefa calcular quadrado')

t1 = Thread(target=calcular_cubo, args=(5, 3))
t2 = Thread(target=calcular_quadrado, args=(5, 2))

t1.start()
t2.start()


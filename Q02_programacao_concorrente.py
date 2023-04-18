#Questão 02: Implementaar uma solução em Python, através do uso da thread, que faça:
# a) Inicie a execução de duas Thread;
# b) Coloque a primeira e a segunda thread para esperar 3 e 2 segudndos;
# c) Informar a ordem de execucao das threads

from time import sleep
from threading import Thread

def tarefa(tempo_espera, nome_tarefa):
    print(f'Iniciando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusao da tarefa {nome_tarefa}')


t1 = Thread(target=tarefa, args=(3,'A'))
t2 = Thread(target=tarefa, args=(2,'B'))

t1.start()
t2.start()

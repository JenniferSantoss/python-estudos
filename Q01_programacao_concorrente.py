#Questão 01: Implementaar uma solução em Python, através do uso da thread, que faça:
# a) Inicie a execução de uma Thread;
# b) Coloque a Thread para esperar 2 segundos;
# c) Informe o inicio e o final da execução de uma Thread.


from time import sleep
from threading import Thread

def tarefa(tempo_espera, mensagem):
    print(f'Iniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusao da tarefa {mensagem}')

thread = Thread(target=tarefa, args=(2, 'Thread em execucao'))
thread.start()


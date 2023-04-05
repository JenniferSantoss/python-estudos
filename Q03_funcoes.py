# Questão 03: Implementar uma solção que calcule o fatorial de um numero

def fatorial(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f

n = 5
print(f'Resultado: {fatorial(n)}')
    

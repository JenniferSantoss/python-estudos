# Estudando sobre Orientação a objetos em Python 

class Pessoa:
    def __init__(self, nome, idade) : #construtor
        self.nome = nome    #atributos
        self.idade = idade

    def imprimir(self):   #metodos
        print(self.nome, "tem", self.idade, "anos")

    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade = idade


p = Pessoa ("Ana", 25)        
p.imprimir()

# Estudando sobre Orientação a objetos em Python (Conceito de Herança e Polimosfirmo)

from orientacao_objetos import Pessoa

class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao

    def imprimir(self):
        super().imprimir()
        print("\t e trabalha como", self.profissao)


p = Profissional("Ana", 25, "balconista")        
p.imprimir()
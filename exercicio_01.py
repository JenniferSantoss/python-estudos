# Questão 01: Item a) Implementar um programa python para criar uma classe veículo com atributos de instância "velocidade máxima" e "km por litro"

class Veiculo:
    def __init__(self, nome, velocidade_maxima, km_litro):
        self.nome = nome
        self.velocidade_maxima = velocidade_maxima
        self.km_litro = km_litro

    def Imprimir(self):
        print(f'nome = {self.nome}')
        print(f'Velocidade maxima = {self.velocidade_maxima}')
        print(f'Quilometros por litro = {self.km_litro}')

modelo_carro = Veiculo('fusca', 180, 10)
modelo_carro.Imprimir()


# Item b) crie uma classe filha "onibus" que herdará todas as variáveis e métodos da classe "veiculo" e passe o número de assentos.

class Onibus(Veiculo):
    def capacidade_assentos(self, capacidade):
        print(f'A capacidade de assentos de {self.nome} e {capacidade}')

onibus_escolar = Onibus('Scania', 120, 8)
onibus_escolar.Imprimir()
onibus_escolar.capacidade_assentos(70)

# Questão 04: Implementar uma solução python que determine o valor a ser pago em um taxímetro

def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * 
    km_rodado) * multiplicador
    return valor


pagamento = taximetro(3.5)
print(pagamento)



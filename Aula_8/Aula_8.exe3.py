km_percorridos=float(input('Quantos Km/s esse carro percorreu?'))
dias_alugado=float(input('Quantos dias foi alugado?'))
preço_carro= (60*dias_alugado)+(0.15*km_percorridos)
print('O valor do carro acabará saindo por R${:.2f}'.format(preço_carro))


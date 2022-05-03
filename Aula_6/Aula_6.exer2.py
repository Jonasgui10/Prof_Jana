velo= int(input('Qual a velocidade do carro na pista?'))
if velo> 80:
    multa= velo-80
    multamulta=multa*7
    print('A multa é de {:.2f} reais.' .format(multamulta))
else:
    print('Sem multa vinculada a velocidade')

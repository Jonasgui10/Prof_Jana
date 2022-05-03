maior=0
menor=0

'''for c in range(0,5):
    peso=float(input('Diga seu peso: '))
    if c==1:
        maior=peso
        menor=peso
    else:
        if maior<peso:
            maior=peso
        elif menor>peso:
            menor=peso
print('O maior peso é {}, já o menor é {}'. format(maior, menor))  ''' 


maior=0
menor=0
for p in range (1,6):
    peso=float(input('peso da {} pessoa:' .format(p)))
    if p==1:
        maior=peso
        menor=peso
    else:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))

           



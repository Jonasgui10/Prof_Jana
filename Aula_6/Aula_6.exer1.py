from random import randint

i=randint(0,5)
x=int(input('Digite um numero inteiro de 0 a 5?'))
if i==x:
    print('Parabéns você acertou')
else:
    print('Você errou, tente novamente')
from random import randint 
x=int(input('Vamos jogar pedra, papel e tesoura: \n1.Pedra \n2.Papel \n3.Tesoura'))
r=randint(1,3)
if r == 1:

    if x == 1:
        print('empate')
    elif x == 2:
        print('Você ganhou')
    elif x == 3:
        print('Você perdeu')
elif r == 2:
    if x == 1:
        print('Você ganhou')
    elif x == 2:
        print('Empate') 
    elif x == 3:
        print('Você perdeu')
elif r == 3:
    if x == 1:
        print('Você ganhou')
    elif x == 2:
        print('Você perdeu')
    elif x == 3:
        print('Empate')                       


            
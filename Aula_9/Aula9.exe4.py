ano_nascimento= int(input('Qual ano de nascimento? '))
idade= 2022-ano_nascimento
passou= idade-18
alistamento=18-idade

if idade>18:
    print('Já passou de época, seu alistamento foi a {} anos átras'.format(passou))
if idade<18:
    print('Ainda não está na hora de se alistar, falta {} anos'.format(passou))
if idade == 18:
    print('Está na hora de se alistar')
    
        
ano_nascimento=int(input('Qual data de nascimento do atleta? '))
idade=2022-ano_nascimento

if idade<=9:
    print('mirim')

elif idade>9 and idade<14:
    print('Infantil')

elif idade>14 and idade<19:
    print('Junior')

elif idade>19 and idade<=25:
    print('Senior')

elif idade>25:
    print('Master')
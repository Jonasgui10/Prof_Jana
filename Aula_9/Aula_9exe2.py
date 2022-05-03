num1= int(input('Diga um numero inteiro :'))

print('\n 1.Número binário \n 2.Número octal \n 3.Número decimal')
opção= int(input('Escolha uma opção: '))

if opção<1 or opção>3:
    print( 'Opção invãlida')
elif opção == 1:
    bi= bin(num1)
    print('A forma binário do  {} é {}'. format(num1,bi))

elif opção == 2:
     octal= oct(num1)
     print('A forma octal do {} é {}'.format(num1, octal))

elif opção == 3:
    hexadecimal= hex(num1)
    print('A forma hexadecimal do {} é {}'.format(num1, hexadecimal))


hipotenusa=int(input('Comprimento da reta?'))
adjacente=int(input('Comprimento da reta?'))
oposto=int(input('Comprimento da reta?'))

if hipotenusa>adjacente+oposto:
    print('não Pode formar o triangulo')

else:
    print(' pode formar o triangulo')

    if adjacente>hipotenusa+oposto:
        print('nao Pode formar o triangulo') 
    else:
        print('pode formar o triangulo')
        if oposto>hipotenusa+adjacente:
            print('nao Pode formar o triangulo') 
        else:
            print(' pode formar o triangulo')              
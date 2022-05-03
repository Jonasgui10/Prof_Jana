print('\n1.Tensão, o programa deve solicitar que ele informe os valores de resistência e Corrente \n2.Resitência, o programa deve solicitar que ele informe os valores da tensão e da Corrente \n3.Corrente, o programa deve solicitar que ele informe os valores da Tensão e da Resistência')
opção=int(input('Escolha uma opção :'))

if opção<1 or opção>3:
    print('Opção inválida')
elif opção == 1:
    res=float(input('Informe o valor da resistência :')) 
    cor=float(input('Informe o valor da corrente: '))
    tensão=res*cor
    print('O valor da tensão é {} volts'.format(tensão))

elif opção == 2:
    tes=float(input('Informe o valor da tensão :'))
    cor=float(input)('Informe o valor da corrente :')
    resistencia=tes/cor
    print('O valor da resistencia é {} ohm '.format(resistencia))

elif opção == 3:
    tes=float(input('Informe o valor da tensão: '))
    res=float(input('Informe o valor da resistencia: '))
    corrente=tes/res
    print('O valor da corrente é {} ampére'.format(corrente))


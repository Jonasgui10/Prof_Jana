peso=float(input('Qual seu peso? '))
altura=float(input('Qual sua altura'))
imc=peso/(altura**2)

if imc<18.5:
    print('Seu peso está abaixo do recomendado! ')

elif imc<=18.5 and imc<25:
    print('Seu peso está ideal! ')
elif imc<=25 and imc<30:
    print('Você está com sobrepeso! ') 
elif imc<=30 and imc<40:
    print('Você tem obesidade!')
elif imc>=40:
    print('Obesidade morbida! ')           
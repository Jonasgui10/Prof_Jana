num1= int(input('Digite um número inteiro: '))
num2= int(input('Digite um número inteiro: '))

maior=num1
if num2>maior:
    maior=num2
if num1 == num2:
    print('Nenhum número é maior')
else:
    print('O maior número é {}'.format(maior))    


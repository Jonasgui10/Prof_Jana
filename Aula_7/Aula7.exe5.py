num= float(input('Digite um numero: '))
num2= float(input('Digite outro numero'))

print('\n 1. Média ponderada, com o pesos 2 e 3, respectivamente  \n 2. Quadrado da som de 2 numeros \n 3. Cubo do maior número {}')
op=int(input('Escolha uma opção'))

if op<1 or op>3:
    print('Opção inválida')
elif op ==1:
    media = (num*2+num2*3)/5
    print('Média ponderada calculada: {:.2f}'.format(media)) 
elif op == 2:
    quadrado =(num+num2)**2
    print('Quadrado da soma dos números: {:.2f}'.format(quadrado)) 
elif num<num2:
        cubo=num**3
        print(' {} é o menor e seu cubo é {}'.format(num, cubo))  
else:
    cubo=num2**3
    print(' {} é o menor e seu cubo é {}'.format(num2,cubo))                
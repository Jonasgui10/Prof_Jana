from Aula28_ex00 import *

escolha=int(input('Escolha uma das opções: \n1.Soma \n2.Subtração \n3.Divisão \n4.Multiplicação \n5.Todas as opções'))

num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))

if escolha<0 or escolha>5:
    esc=int(input('Opção inválida.'))
elif escolha == 1:
    s=soma(num1,num2) 
    print(f'A soma dos dois números é {s}')
elif escolha == 2:
    s2=subtracao(num1,num2)
    print(f' A subtração entre dois números é {s2}')
elif escolha == 3:
    d=divisao(num1,num2)
    print(f'A divisão entre dois números é igual  {d}')
elif escolha == 4:
    mm=multiplicacao(num1,num2)
    print(f'A multiplicação entre dois números é  igual {mm}') 
elif escolha == 5:
    c=calculadora(num1,num2)
    print(f'Soma={c[0]}, Subtração={c[1]}, Divisão={c[2]}, Multiplicação={c[3]} ')


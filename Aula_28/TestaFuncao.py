from Minhas_funcoes import *

print('Calculo das areas de figuras geometricas: ')
escolha=int(input('Escolha uma das opções: \n1.circulo \n2.triângulo \n3.retângulo'))

num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))

if escolha<0 or escolha>3:
    esc=int(input('Opção inválida.'))
elif escolha == 1:
    ac=calcula_area_circulo(num1,num2) 
    print(f'Area do circulo é {ac}')
elif escolha == 2:
    at=calcula_area_triangulo(num1,num2)
    print(f'Area do trinagulo é {at}')
elif escolha == 3:
    ar=calcula_area_retangulo(num1,num2)
    print(f'Area do retangulo é {ar}')


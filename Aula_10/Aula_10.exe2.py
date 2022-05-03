x1=float(input('Informe o comprimento da primeira reta: '))
x2=float(input('Informe o comprimento da segunda reta: '))
x3=float(input('Informe o comprimento da terceira reta: '))
if x1<x2+x3 and x2<x1+x3 and x3<x2+x1:
    print('É possível formar um triângulo. ')
    if x1==x2 and x1==x3 and x2==x3:
        print('Triângulo equilatero. ')
    elif x1!=x2 and x1!=x3 and x3!=x2:
        print('Triângulo escaleno. ')
    else:
        print('Triângulo isoceles. ')
else:
    print('Não podem formar um triângulo. ')        

       

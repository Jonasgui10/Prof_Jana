n=int(input('Digite a quantidade de numeros a informar: '))

soma=0

for cont in range(n):
    num=float(input('Digite um numero: '))
    soma+=num#soma = soma +1
media=soma/n
print('Média= {:.2f}'.format(media))
    
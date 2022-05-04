'''Ex 3. Crie um programa que leia um valor N, tal que N > 0. O programa deve gerar duas listas aleatórias (L1 e L2), com valores no intervalo
[1 e 10]. A terceira lista, L3, deve ser gerada com base na soma entre os elementos de L1 e de L2. Ao fim, o programa deve imprimir as 3
listas.'''

from random import randrange

n=int(input('Informe o valo de N: '))

if n>0:
    l1=[randrange(1,11) for i in range(n)]
    l2=[randrange(1,11) for i in range(n)]

    l3=[]

    for i in range(n):
        l3.append(l1[i]+l2[i])

    print(f'L1 = {l1}') 
    print(f'L2 = {l2}') 
    print(f'L3 = {l3}')  
else:
    print('Erro: N deve ser maior que 0 ')
        
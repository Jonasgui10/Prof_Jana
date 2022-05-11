'''Ex 5. Crie um programa que gere, aleatoriamente, uma matriz M, com elementos no intervalo [0, 1]. A
quantidade de linhas e de colunas de M devem ser informadas pelo usuário. Ao fim, o programa deve
informar se M é uma matriz nula.'''

from random import randrange
linha=int(input('Diga o numero de linhas da matriz'))
coluna=int(input('Diga o numero de colunas da matriz'))
m=[]
soma=0
for i in range(linha):

    for c in range (coluna):
        n=randrange(0,2)
        m.append(n)


for s in m:
    soma+=s
    if soma == 0:
        print(f'A matriz {m} é nula ') 
    else:
        print(f'A matriz{m} não é nula')  
print(f'O numero de linhas é {linha}')
print(f'O numero de colunas é {coluna}')                

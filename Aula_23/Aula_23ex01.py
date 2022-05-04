'''Ex 1. Crie um programa para gerar duas matrizes quadradas aleatórias (A e B), no intervalo [1, 10], de mesma ordem, a qual deve ser
informada pelo usuário. Ao fim, o programa deve calcular e imprimir a soma entre os elementos de A que estão abaixo da diagonal
principal com os elementos de B que estão acima da diagonal principal.'''


from random import randrange

linha=int(input('Números de linhas: '))
coluna=int(input('Número de colunas: '))

a=[[randrange(1,11) for i in range(coluna)] for j in range (linha)]
b=[[randrange(1,11) for i in range(coluna)] for j in range (linha)]

abaixodp=0
acimadp=0

for i in range(linha):
    for j in range(coluna):
        if i>j:
            abaixodp+=a[i][j]
        if i<j:
            acimadp+=b[i][j]

print(' Matriza A: ')
for i in range(linha):
    for j in range(coluna):
        print(a[i][j], end=' ')
    print()

print(' Matriza B: ')
for j in range(linha):
    for i in range(coluna):
        print(b[j][i], end=' ')
    print()
print(f'Soma= {abaixodp+acimadp}') 
          





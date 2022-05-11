'''Ex 3. Crie um programa que leia um valor N, tal que N > 1. O programa deve gerar, aleatoriamente, uma
lista L. Por fim, o programa deve calcular e imprimir a média geométrica dos N elementos da lista.'''

from random import randrange
from math import sqrt

n=int(input('Escreva um valor para N: '))

if n>1:
    lista=[randrange(1,11) for i in range (n)]

    maior=max(lista)
    menor=min(lista)
    media=sqrt(maior*menor)

print(lista)
print(f'A média geometrica dos elementos N é {media}')    




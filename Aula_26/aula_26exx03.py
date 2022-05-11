'''Ex 3. Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o
maior.'''

import random
def maior(lista):
    nmaior=max(lista)
    return nmaior

lista=[]
l=0

while l < 10:
    a=random.randint(0,10)
    lista.append(a)
    l=l+1

print(f'O maior valor da {lista} é {maior(lista)} ')    



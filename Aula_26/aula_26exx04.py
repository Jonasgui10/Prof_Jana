'''Ex 4. Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somapar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e
a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função
anterior.'''
import random

def sorteia():
    
    numeros=[]
    l=0  
    
    
    while l < 5:
        n=random.randint(0,10)  
        numeros.append(n)
        l=l+1
    return numeros 

def somapar(lista):
    l=0
    print(lista)

    lista2=[]

    for l in lista:
        if l %2==0:
            lista2.append(l)
    print(sum(lista2))

somapar(sorteia())       

from random import randint

def sorteia(lista):
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)

def somapa(lista):
    soma=0
    for valor in lista:
        if valor %2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista},  temos {soma}')

numeros=list()
sorteia(numeros)
somapar(numeros)

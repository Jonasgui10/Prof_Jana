'''numeros=[]
numerop=[]

for t in range(4):
    numero=int(input('Escreva um numero? '))
    numeros.append(numero)
    if numero %2 == 0:
        numerop.append(numero)



print(f'{numeros.count(9)}')
print(f'{numeros.index(3)}')
print(f'Os números pares são {numerop}')'''

# Usando a tupla

'''num=int(input('Digite um número: ')), int(input('Digite um outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))

if 9 in num:
    print(f' O valor apareceu {num.count(9)} vezes ')
else:
    print(' O númerpo 9 não foi informado. ') 
if 3 in num:
    print(f' O número 3 foi digitado na {num.index(3)+1} posição. ') 
else:
    print('O número 3 não foi informado. ') 
for n in num:
    if n%2==0:
        print(n, end= ' ')   '''

#Utilizando lista de estrutura de dados

'''num=[]

for n in range(0,4):
    num.append(int(input('Digite um número: ')))
if 9 in num:
    print(f' O valor apareceu {num.count(9)} vezes ')
else:
    print(' O númerpo 9 não foi informado. ') 
if 3 in num:
    print(f' O número 3 foi digitado na {num.index(3)+1} posição. ') 
else:
    print('O número 3 não foi informado. ') 
for n in num:
    if n%2==0:
        print(n, end= ' ') '''


                  






'''Ex 4. Faça um programa que ajude um jogador da Mega Sena a criar palpites. O programador vai
perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.'''

import random

lista=[]
jogo=int(input('Quantos jogos você quer: '))
for i in range(jogo):
    for i in range(6):
        num=random.randrange(1,60)
        lista.append(num)
    print(f'jogo {1+i} os numeros sorteados são {lista}')
    lista.clear()    





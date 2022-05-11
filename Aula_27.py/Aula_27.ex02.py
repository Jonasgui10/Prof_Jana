'''Ex 2. Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de
mostrar a ficha do jogador, mesmo que alguns dados não tenham sido informados
corretamente.'''

def ficha(jog, gol):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato. ')

n=input('Nome do jogador: ') 
g=input('Número de gols: ')

if g.isnumeric():
    g=int(g)

else:
    g=0

if n.strip()==' ':
    ficha(gol=g)

else:
    ficha(n,g)

if type(n)==int:
    print('Sim')
else:
    print('Não')
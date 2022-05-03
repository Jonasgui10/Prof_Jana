'''from random import shuffle , choice
rifas=[]
escolhido=' '

for r in range(4):
    mrifa=input('Nome da pessoa que comprou a rifa :')
    rifas.append(mrifa)

shuffle=rifas
escolhido=choice(rifas)

print(escolhido)'''

from random import shuffle, choice

rifa=[]

while True:
    nome=input('Informe o nome da pessoa que comprou a rifa: ')
    rifa.append(nome)
    resp=input('Deseja continuar [S/N]? ')
    if resp.upper()== 'N':
        break
shuffle(rifa)
sorteado=choice(rifa)

print(f' O ganhador da rifa foi o {sorteado}')





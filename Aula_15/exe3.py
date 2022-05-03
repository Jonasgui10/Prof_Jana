from email.errors import InvalidDateDefect


somaidade=0
maioridadehomem=0
nomemmaisvelho=''
mulhermenor=0
mediaidade=0

for c in range(0,4):
    nome=input('Nome: ').strip()
    idade=int(input('Idade: '))
    sexo=input('Sexo [F/M]: ').strip().upper()
    
    somaidade+=idade
    if c==1 and sexo in 'M':
        maioridadehomem=idade
        nomemaisvelho=nome

    if sexo in 'M' and idade>maioridadehomem:
        maioridadehomem=idade
        nomemaisvelho=nome
    if sexo in'F' and idade<20:
        mulhermenor+=1   

mediaidade=somaidade/4

print('A média de idade do grupo é de {} anos. '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'. format(maioridadehomem,nomemmaisvelho))
print('{} mulheres tem mais de 20 anos '.format(mulhermenor))

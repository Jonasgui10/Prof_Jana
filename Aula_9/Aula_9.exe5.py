nota1=float(input('Qual a nota do aluno? '))
nota2=float(input('Qual a segunda nota do aluno? '))

media=(nota1+nota2)/2

if media<5:
    print('Sua média foi {}, você está rerovado'. format(media))
if media>=5 and media<=6.9:
    print('Sua média ficou {} , você está de recuperação'.format(media))
if media>=7:
    print('Sua média foi {} , parabéns você foi aprovado'.format(media))        
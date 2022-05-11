'''Ex 4. Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o
comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘Fim’, o programa
encerrará. OBS.: use cores.'''

c=('\033[m', '\033[0;30;41m', '\033[0;30;42m' , '\033[0;30;43m' , '\033[0;30,44m' , '\033[0;30,45m' '\033[0;30,46m')

def ajuda(com):
    titulo(f'Acessando o manual de comandos {com}',4)
    print(c[6], end=' ')
    help(com)
    print(c[0], end=' ')

def titulo (msg, cor=0):
    tam=len(msg)+4
    print(c[cor], end=' ')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[0], end=' ')

comando=' ' 
while True:
    titulo('Ajuda Python', 2)
    comando=input('Função ou Bibliotecas: ')
    if comando.upper()=='Fim':
        break
    else:
         ajuda(comando)   


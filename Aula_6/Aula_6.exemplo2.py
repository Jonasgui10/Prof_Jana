print('##Programa de emrepstimos ## \n Responde: 0 - Não e 1 - sim')
nomenegativado = int(input('Possuí nome negativado?'))

if nomenegativado == 1:
    print('Não pode realizar o emprestimo.')
else:
    carteiraassinada = int(input('Possuí carteira assinada?'))
    if carteiraassinada ==  0:
        print('Não pode realizar o emprestimo.')
    else:
        possuicasapropria = int(input('Possui casa propria?'))
        if possuicasapropria == 0:
            print('Não pode realizar o emprestimo.')
        else:
            print('Concede o emprestimo')
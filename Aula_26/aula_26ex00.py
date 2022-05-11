def exibirMensagem():
    print('Python é fácil')

#Programa principal
#exibirMensagem()

def exibirMensagemBoasVindas(pessoa, mensagem):
    print(f'{mensagem} {pessoa}')

exibirMensagemBoasVindas('Janaína', 'Bem-vinda')

exibirMensagemBoasVindas()

def exibirMensagemBoasVindas(pessoa= 'Fulano', mensagem='Bem=vindo'):
    print(f'{mensagem}, {pessoa}')

exibirMensagemBoasVindas()


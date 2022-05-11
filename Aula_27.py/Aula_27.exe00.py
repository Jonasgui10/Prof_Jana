'''def escreve(msg):
    """
    Print de mensagem informado peo usuário
    msg: entrada do usuário para programa
    """
    print('~')
    print(msg)
    print('~')
escreve(input('Digite uma frase: ')) 

help(escreve)'''

def teste(b):
    b+=4
    c=2
    print(f'A dentro da função vale {a} ')
    print(f'B dentro da função vale {b} ')
    print(f'C dentro da função vale {c} ')
#Programa principal
    
a=5 # Variavél de escopo global
teste(a)
print(f'A fora de unção vale {a} ')


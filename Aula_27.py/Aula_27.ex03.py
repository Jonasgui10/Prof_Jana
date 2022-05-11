'''Ex 3. Crie um programa que tenha a função leialnt(), que vai funcionar de forma semelhante à
função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex.: leialnt(‘Digite um n’)'''

def LeiaInt(msg):
    ok=False
    valor=0
    
    while True:
        n=input(msg)
        if(n.isnumeric(msg)):
            valor=int(n)
            ok=True
        else:
            print('Digitar um número válido: ')
        if ok:
                  Return valor
n=LeiaInt('Digite um número: ') 
print(f'Você acabou de digitar o número {n}')   






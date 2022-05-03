from socket import NI_NUMERICHOST


num = soma = cont = 0
num=int(input('Digite um número ou 999 para parar: '))

while True:
    if num != 999:
        soma+=num
        cont+=1
    else:
        break  
    num=int(input('Digite um número ou 999 para parar: '))
print(f'Foram digitados {cont} numeros e a soma desses números resultou no valor de {soma}')
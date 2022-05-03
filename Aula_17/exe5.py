total=totmil=menor=contador=0

barato=' '
while True:
    produto=input('Nome do produto: ')
    preco=float(input('Preço R$: '))
    contador+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if contador==1 or preco<menor:
        menor=preco
        barato=produto
    resposta=' ' 
    while resposta not in 'SN':
        resposta=input('Quer  continuar [S/N]').strip().upper() 
    if resposta == 'N':
        break
print(f'O total das compras foi R${total:.2f}') 
print(f'Temos {totmil} produtos custando  mais de R$ 1000,00. ')
print(f'O produto  mais barato foi o {produto}  que custa R${menor:.2f} ')         

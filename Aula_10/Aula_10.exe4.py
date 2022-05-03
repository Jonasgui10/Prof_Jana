produto=float(input('Qual o valor do produto que você irá comprar? '))
print('\n1.à vista/cheque:10 desconto. \n2.á vista no cartão:5 desconto \n3.até 2x no cartão:preço normal.')

opção=int(input('Escolha uma opção de pagamento! '))
if opção<1 or opção>3:
    print('Opção inválida')

elif opção == 1:
    vista_cheque= produto*0.10
    desconto=produto-vista_cheque
    print('O produto no valor de R${:.2f} , recebeu um desconto e acabou saindo por este valor R${:.2f}'.format(produto, desconto))
elif opção == 2:
    vista_cartão=produto*0.05
    desconto1=produto-vista_cartão
    print('O produto no valor de R${:.2f} , recebeu um desconto e acabou saindo por este valor R${:.2f}'.format(produto, desconto1))
elif opção == 3:
    print('O valor no cartão em 2x ficou no valor de {:.2f}'.format(produto))


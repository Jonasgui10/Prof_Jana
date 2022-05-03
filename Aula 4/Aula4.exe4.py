sal_base=float(1500)
comissao=float(200)

nome=input('qual o nome do corretor?')
vendas=int(input('Quantos imoveis foram vendidos?'))
Total_vendas=float(input('informe o valor total de vendas do corretor R$'))

sal_final=sal_base+(comissao*vendas) + (Total_vendas*0.05)
print('Salario final do corretor {} é de R${:.2f}.'.format(nome, sal_final))



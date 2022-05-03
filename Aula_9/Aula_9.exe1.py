casa= float(input('Qual o valor da casa?'))
salário_comprador= float(input('Qual salário do comprador?'))
anos_pagamento= float(input('Quantos meses pagamento do empréstimo?'))

prestação= casa/anos_pagamento
presta= salário_comprador*0.30

if prestação >= presta:
    print('Não pode realizar o emprestimo')
else:
    print('Pode realizar o emprestimo')    
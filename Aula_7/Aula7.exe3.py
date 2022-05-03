salário=float(input('Qual o salário do funcionário?'))
aumento=salário*0.15 if salário<=1250 else salário*0.10
salario_f=salário+aumento
print('o aumento do salário será R${:.2f} , totalizando o valor de R${:.2f}'.format(aumento, salario_f))
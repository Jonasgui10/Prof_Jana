sal_base=float(input('Qual salário do funcionário? '))
print('\n1.Programador de sistemas \n2.Analista de sistemas \n3.Analista de banco de dados')

opção=int(input('Escolha um dos cargos a seguir para dar sequência ao processo: '))
if opção<1 or opção>3:print('Cargo inválido')

elif opção == 1:
    aumento= sal_base*0.30
    sal_final=sal_base+aumento
    print('O novo salário do Programador de Sistemas será R${:.2f}'.format(sal_final))
elif opção == 2:
    aumento2= sal_base*0.20
    sal_final2=sal_base+aumento2
    print('O novo salário do Analista de Sistemas será de R${:.2f}'.format(sal_final2))
elif opção == 3:
    aumento3=sal_base*0.15
    final_sal3=sal_base+aumento3
    print('O novo salário do Analista de Banco de Dados será de R${:.2f}'.format(final_sal3))       
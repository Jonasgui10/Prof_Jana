valor_camisa=float(input('Valor da camisa? '))
num_vendidas=float(input('Numero de camisetas vendidas? '))

if num_vendidas<=5:
    des_a=valor_camisa*0.03
    a=valor_camisa-des_a
    final_a=(num_vendidas*a)
    print('A compra da camisa com desconto saiu pelo valor de R${:.2f}, e o valor total delas R${:.2f}'.format(a, final_a))
elif num_vendidas>5 and num_vendidas<=10:
    des_b=valor_camisa*0.05
    b= valor_camisa-des_b
    final_b=(num_vendidas*b)
    print('A compra da camisa com desconto saiu pelo valor de R${:.2f} ,e o valor total delas R${:.2f}'.format(b, final_b)) 
elif num_vendidas>10:
    des_c=valor_camisa*0.07
    c=valor_camisa-des_c
    final_c=(num_vendidas*c)
    print('A compra da camisa com desconto saiu pelo valor R${:.2f}, e o valor total delas R${:.2f}'.format(c, final_c))      
    
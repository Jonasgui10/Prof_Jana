largura=float(input(' Qual a largura da parede?'))
altura=float(input('Qual a altura da parede?'))
a=altura*largura
tinta= a/4
print('A aréa desta parede é de {:.2f}m e a tinta necessario para pintar será {:.2f} litros.'.format(a,tinta))
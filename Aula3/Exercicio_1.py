# Exercicio 1
print('Exercicio 1')
inteiro=float(input('numero inteiro?'))
print('antecessor', inteiro-1)
print('sucessor', inteiro+1)
# Exericio 1 maneira 2
num=int(input('digite um valor?'))
ant=num-1
suc=num+1
print('Analisando o valor {}, seu antecessor é {} e o seu sucessor é {}'.format(num,ant,suc))
      
# Exercicio 2
print('Exercicio 2')
algoritimo=float(input('digite um algoritimo?'))
dobro=algoritimo*2
triplo=algoritimo*3
raiz=algoritimo**(1/2)
print('o dobro do numero é',dobro, 'o triplo do numero',triplo,'raiz do numero',raiz)
# Exercicio 2 maneira 2
n=int(input('digite um numero?'))
d=n*2
t=n*3
r=n**(1/2)
print('O dobro de {} vale {}. \n O triplo de {} vale {}. \n A raiz quadrada de {} é igual a {}.'.format(n,d,n,t,n,r))
          
# Exercicio 3
print('exercicio 3')
deslocamento=float(input('Variação de um objeto em metros?'))
tempo=float(input('Variação do tempo percorrido em segundos?'))
media=deslocamento/tempo
print('a velocidade média é', media, 'm/s')
# Exercicio 3 maneira 2


# Exercicio 4
print('Exercicio 4')
preço=float(input('Preço unitário?'))
venda=float(input('Quantidade vendida?'))
lucro=(preço*venda)*0.05
print('a comissão dos funcionários sera de: {:.2f}.'.format(lucro))

# Exercicio 5 maneira 2
pi=float(3.14)
raio=float(input('digite o raio da área de convivência?'))
area=pi*(raio**2)
print('area igual a {}.'.format(area))           


        
              

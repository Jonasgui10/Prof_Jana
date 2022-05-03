'''dias=('domingo' , 'segunda' , 'terca' , 'quarta' , 'quinta' , 'sexta' , 'sabado' )

print(type(dias))

print(dias[3])'''

'''texto='python'
print(tuple(texto))'''

'''lista=[1,2,3,4]
lista[0]=9
print(tuple(lista))'''

'''lista=[3,5]
tupla1=(1,2,lista)
tupla2=(1,2,lista[0],lista[1])

#print(tupla)

#print(tupla[2])

#print(len(tupla2))'''

'''print(tupla2.count(2))'''

'''lista=['python' , 1, 2, 'java']
print(lista)'''

'''meses= ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezembro']
n=1
while n<4:
    mes=int(input(' Escolha um mês [1-12]: '))
    if 1<mes<13:
        print(f'O mês é {meses[mes-1]}')
    n+=1    '''

#para tirar iniciar ou final/a partir ou antes
'''meses= ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezembro']
print(meses[:-3])'''

'''meses= ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezembro']
meses.append('Jonas')
#adiciona algo a lista
print(meses)'''

'''meses= ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezembro']
print(meses*2)#dobrar meses '''


'''meses= ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezembro']
meses+=['jonas', 'josé']
print(meses)'''
#adcionar dois nomes


'''meses= ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezembro']
for mes in meses:
    print(mes)'''
#um abaixo do outro    


meses= ['janeiro' , 'fevereiro' , 'março' , 'abril' , 'maio' , 'junho' , 'julho' , 'agosto' , 'setembro' , 'outubro' , 'novembro' , 'dezembro']
for mes in meses:
    print(mes, end=' ')
#na mesma linha











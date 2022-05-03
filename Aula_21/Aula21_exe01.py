lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
maiovalor=lista[0]
menorvalor=lista[0]
listaPares=[]
ocorrencia=0
mediaElementos=0
somaNegativo=0



for index in range(0,len(lista)):
    #maior valor
    if maiovalor<lista[index]:
        maiovalor=lista[index]
    #menor valor
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    #lista numeros pares
    if lista[index]%2 == 0:
        listaPares.append(lista[index])#listaPares=[12] 
    #ocorrencia primeiro elemento
    if lista[index] == lista[0]:
        ocorrencia+=1  
    mediaElementos+=lista[index]
    #Soma numeros negativos
    if lista[index]<0:
        somaNegativo+=lista[index]







# média
mediaElementos/=len(lista)        
             









print(f'Maior valor: {maiovalor}')
print(f'Menor valor: {menorvalor}')
print(f'Números pares: {listaPares}')
print(f'Número de ocorrências do primeiro elemento: {ocorrencia}')
print(f'Média elementos: {mediaElementos}')
print(f'Elementos negativos: {somaNegativo}')





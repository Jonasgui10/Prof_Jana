lista = ['janaina' , 'josé' , 'maria' , 'carlos']
listaa = ['josé' , 'jonas']

#for n in range(0, len(lista)): loop lista
#lista.append('jorge') adiciona no final
#lista.insert(0, 'jorge') adiciona na posiçao indicada
#lista.sort() ordena ordem crescente
#lista.sort(reverse=True) decrescente
#del lista[-1] tira o ultimo
#lista.remove('janaina') indica
#lista.pop(3) indica ou vazio ultimo elemento
#lista.clear() imprimi lista vazia

#listaa=lista vincula uma lista na outra
#listaa=lista[:] lista.append('josé') atribui a listaa mas não a lista

#listaa=lista lista.extend(listaa) adiciona uma lista a outra

#print(lista.count('josé')) quantas vezes aparece no vetor

#print(lista.index('janaina')) indica lugar que está numeração

#for indice, nome in enumerate(lista): vai indicar o indice de cada nome
    #print(f'{nome} está armazenado no indice {indice} ')


a = [[2, 1, -5,],[3, 7, 0],[6, 4 ,8]]
#print(a[0][1]) imprime a coluna de tal cordenada
#print(a[0][0]+a[0][1]+a[0][2]) soma de todos os numeros
#print(a[0][0], a[0][1], a[0][2]) mostrar os valores
soma_a=0
lin=len(a)
col=len(a[0])

for i in range(lin):
    for j in range(col):
        soma_a+=a[i][j]
print(soma_a)        


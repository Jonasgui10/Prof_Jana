'''Ex 4. Um professor de Matemática deseja construir um programa para gerar uma Progressão Aritmética (PA). Para isso, devem ser
informados 3 parâmetros de entrada: a) primeiro termo da PA, b) quantidade de termos da PA e c) razão dessa PA. Construa um programa
para carregar e imprimir uma lista contendo os termos da PA, bem como a soma dos elementos da PA.'''


termo=int(input('Informe o 1 termo da P.A. '))
num_termos=int(input('Informe o número de termos da P.A. '))
razao=int(input('Informe a razão.  '))
pa =[termo]

termo_anterior=termo

for x in range(num_termos-1):
    termo_atual=termo_anterior+razao
    pa.append(termo_atual)
    termo_anterior=termo_atual
print(pa)

soma=sum(pa)

print(f'Soma dos elementos da PA = {soma}')
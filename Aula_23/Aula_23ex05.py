'''Ex 5. Os professores de Educação Física estão organizando uma seletiva para montar a equipe de natação. Para isso, eles convocaram os
7 melhores tempos da última competição e marcaram o tempo de cada um dos nadadores, na prova dos 25 metros, estilo nado livre.
Considerando que não houve tempos iguais, construa um programa que leia o nome e o tempo (em segundos) de cada atleta e, em
seguida, gere o seguinte relatório: a. nadador com o melhor tempo; b. nadador com o pior desempenho; c. tempo médio dos nadadores e;
Dica: Crie duas listas: uma para cadastrar os nomes dos nadadores e outra para guardar os seus respectivos tempos.'''

atletas=[]
tempo=[]

for x in range(3):
    nome=input('Informe o nome do nadador: ')
    tempos=float(input('Informe o tempo do nadador: '))
    atletas.append(nome)
    tempo.append(tempos)

indice_melhor=tempo.index(min(tempo)) #Imprime o indice do melhor tempo

indice_pior=tempo.index(max(tempo)) #Imprime o indice do pior tempo

media_tempo=sum(tempo)/len(tempo)

print(f'{atletas[indice_melhor]} tem o melhor tempo. ')
print(f'{atletas[indice_pior]} tem o pior tempo. ')
print(f'Média de tempos: {media_tempo:.2f}.  ')


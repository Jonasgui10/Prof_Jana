times= ('Bahia ' , 'Brusque' , 'Chapecoense' , 'CRB' , 'Criciúma' , 'Cruzeiro' , 'CSA' , 'Guarani' , 'Grêmio ' , 'Ituano ' , 'Londrina' , 'Náutico' , 'Novorizontino' , 'Operário-PR' , 'Ponte Preta' , 'Sampaio Corrêa' , 'Sport ' , 'Tombense' , 'Vasco' , 'Vila Nova-GO')
posicao=times.index('Chapecoense')

print(f'Os cinco primeiros times da tabela do basileirão são {times[:5]}')

print(f'Os 4 ultimos colocados da tabela do brasileirão são {times[-4:]}')

print(f'Lista de times : {sorted(times)}')

print(f'O time Chapecoense está na posição {posicao+1}')
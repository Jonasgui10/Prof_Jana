nome=input('Nadador 1: ')
tempo=float(input('Tempo do nadador 1: '))

melhornadador=nome
melhortempo=tempo
piornadador=nome
piortempo=tempo

somatempo=0
somatempo+=tempo
tempo12s15s=0

if 12 <= tempo <=15:
    tempo12s15s+=1

for nadador in range(2,8):
        nome=input(f'Nadador{nadador}: ')
        tempo=float(input(f'Tempo do nadador {nadador} : '))

        if tempo<melhortempo:
            melhornadador=nome
            melhortempo=tempo
        elif tempo>piortempo:
            piornadador=nome
            piortempo=tempo
        somatempo+=tempo

        if 12<=tempo<=15:
            tempo12s15s+=1

print(f'{melhornadador}  é o melhor nadador com {melhortempo} seg. \n{piornadador} é o pior nadador com o pior tempo {piortempo}')

media=somatempo/7

print(f'Média dos tempos = {media:.2f} seg. \nAtletas entre 12 seg e 15 seg : {tempo12s15s}')
            

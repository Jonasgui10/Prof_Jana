'''maior=0
menor=0
for c in range(0,7):
    nascimento=int(input('Digite o ano de nascimento: '))
    if nascimento<=2004:
        maior=maior+1
    else:
        menor=menor+1
print('São maiores de idade {}, e menores de idade {}'.format(maior,menor))   '''  

from datetime import date   
atual=date.today().year
totmaior=0
totmenor=0

for pess in range(1,8):
    nasc=int(input('Em que ano a {} pessoa nasceu?'.format(pess)))
    idade=atual-nasc
    if idade>=18:
        totmaior+=1
    else:
        totmenor+=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('e também tivemos {} pessoas menores de idade'.format(totmenor))            



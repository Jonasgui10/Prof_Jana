frase=input('Forme uma frase: ')
a=frase.count('a')
print('A letra A aparece {} vezes'.format(a))

b=frase.find('a')+1
print('A posição que a letra A aparece pela primeira vez é {}'.format(b))

c=frase.rfind('a')+1
print(' A posição que a letra A aparece pela ultima vez é {}'.format(c))
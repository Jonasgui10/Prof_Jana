'''Ex 2. Crie um programa que tenha uma tupla com várias palavras (não use acentos). Depois disso, você
deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras= ('Amor' , 'Aprender' , 'Sucesso', 'Calmaria' , 'Paz', 'Tristeza')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

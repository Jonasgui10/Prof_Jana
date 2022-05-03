nome_completo=input('Qual seu nome completo? ')
primeiro_nome=nome_completo[0:nome_completo.find("")]
ultimo_nome=nome_completo.split()

print(f'Seu primeiro nome é {primeiro_nome} e seu ultimo nome é {ultimo_nome[len(ultimo_nome)-1]}')



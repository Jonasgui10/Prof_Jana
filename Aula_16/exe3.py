erros=0
for c in range(3,0,-1):
    senha=int(input("senha: "))
    if senha==123456:
        print("Olá, você.Seja bem-vindo ao nosso banco! ")
        break
    elif senha !=123456:
        print('Senha incorreta! Você aind tem {} tentativ(s).'.format(c-1))
        if c ==1:
          print("Sua senha foi bloqueada!Por favor, dirija-se a um de nossos caixas.")

erros=0
while erros < 3:
    senha=int(input("Senha: ")) 
    if senha==123456:
        print("Olá, você.Seja bem-vindo ao nosso banco! ")
        break
    else: #houve erro
    
        erros+=1 #ainda há tentativas
    if erros < 3:   
        print('Senha incorreta! Você aind tem {} tentativ(s).'.format(3-erros))
    else:   
         print("Sua senha foi bloqueada!Por favor, dirija-se a um de nossos caixas.")
         break 

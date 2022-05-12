from Minhas_funcoes import *
'''
# Exercicio 1

print('Calculo das areas de figuras geometricas: ')
escolha=int(input('Escolha uma das opções: \n1.circulo \n2.triângulo \n3.retângulo'))

num1=int(input('Digite o primeiro número: '))
num2=int(input('Digite o segundo número: '))

if escolha<0 or escolha>3:
    esc=int(input('Opção inválida.'))
elif escolha == 1:
    ac=calcula_area_circulo(num1,num2) 
    print(f'Area do circulo é {ac}')
elif escolha == 2:
    at=calcula_area_triangulo(num1,num2)
    print(f'Area do trinagulo é {at}')
elif escolha == 3:
    ar=calcula_area_retangulo(num1,num2)
    print(f'Area do retangulo é {ar}')'''


'''linhas=int(input('Informe as linhas da da matriz: '))
colunas=int(input('Inform a quantidade de colunas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo  inicial: '))
intervalo_final=int(input('Informe o intervalo final: '))'''


'''# Exercicio 2

m=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
print(f'Matriz gerada: {m}')

if len(m)==len(m[0]):
    print(f'Traço da matriz gerada: {calcula_traco_matriz(m)}')
else:
    print('Não é possivel calcular o traço pois não é uma quadrada')   '''

'''# Exercicio 3

a=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
b=gera_matriz_aleatoria(linhas, colunas, intervalo_inicial,intervalo_final)

if len(a)==len(b) and len(a[0])==len(b[0]):
    print(f'Matriz A={a} \n Matriz B: {b} \n Mattriz C (a+b)= {soma_matrizes(a,b)}')
else:
    print('As matrizes não tem a mesma ordem') '''

'''# Exercicio 4

m1=gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
constante=int(input('Informe a constante que multiplicará a matriz gerada: '))
print(f'Matriz gerada:{m1} \nMatriz C (M1 * Constante)= {multiplica_matriz_por_constante(m1, constante)} ' ) '''

# Exercicio 5

cadastro=obtem_dados_funcionario()
print(retorna_num_hom_mul(cadastro))


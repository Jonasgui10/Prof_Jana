Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('olá mundo!')
olá mundo!
print('meu nome é jonas!')
meu nome é jonas!
print('tudo bem com você?')
tudo bem com você?
print(1+5)
6
print(1.6)
1.6
print(1*3)
3
print(5/10)
0.5
print(1-5)
-4
print('1*5)
      
SyntaxError: unterminated string literal (detected at line 1)
print('1*5')
      
1*5
print('1'*'8')
      
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('1'*'8')
TypeError: can't multiply sequence by non-int of type 'str'
print('1'+'5')
      
15
print('1'/'3')
      
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print('1'/'3')
TypeError: unsupported operand type(s) for /: 'str' and 'str'
print('olá',5)
      
olá 5
olá 5
      
SyntaxError: invalid syntax
print('2+2=:',2+2)
      
2+2=: 4
jonas guilherme dos santos
      
SyntaxError: invalid syntax
print(end)
      
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(end)
NameError: name 'end' is not defined
print("value")
      
value
nome='Jonas'
      
idade=24
      
idade='24'
      
nome='Jonas'
      
idade=24
      
altura=1.75
      
print(nome, idade, altura)
      
Jonas 24 1.75
Jonas 24 1.75
      
SyntaxError: invalid syntax





nome='Jonas Guilherme dos Santos'
      
idade=24
      
altura=1.75
      
print(nome, idade, altura)
      
Jonas Guilherme dos Santos 24 1.75
Jonas Guilherme dos Santos 24 1.75
      
SyntaxError: invalid syntax
nome=input('qual o seu nome?')
      
qual o seu nome?Jonas
idade=input('Qual sua idade?')
      
Qual sua idade?24
altura=input('Qual sua altura?')
      
Qual sua altura?1.75
print(nome, idade, altura)
      
Jonas 24 1.75

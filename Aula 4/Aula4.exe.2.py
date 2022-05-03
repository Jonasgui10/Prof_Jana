from math import sqrt
import math
x1=int(input('Qual o x1?'))
y1=int(input('Qual o y1?'))
x2=int(input('Qual o x2?'))
y2=int(input('Qual o y2?'))
p1=(x1-x2)**2
p2=(y1-y2)**2
p1=p1*p1
p2=p2*p2
d=sqrt (p1-p2)
print('Distância entre os pontos: {:.2f}' .format(d))




from math import cos, radians,sin,tan
angulo=float(input('Digite um angulo?'))
seno= sin(radians(angulo))
cons= cos(radians(angulo))
tang= tan(radians(angulo))
print('O seno desse angulo é {:.2f},  o cosseno desse angulo é {:.2f}, a tangente desse angulo é {:.2f}' .format(seno, cons, tang))  

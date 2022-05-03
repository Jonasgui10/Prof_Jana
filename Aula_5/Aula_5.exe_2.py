from math import hypot
cat_oposto=float(input('comprimento do cateto oposto?'))
cat_adjacente=float(input('comprimento do cateto adjacente?'))
hip= hypot(cat_oposto, cat_adjacente)
print('O comprimento da hipotenusa é: {:.2f}.' .format(hip))

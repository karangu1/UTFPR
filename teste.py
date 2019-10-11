import numpy as np
import math

R = 6371e+3
h = 1.76
C = 2*math.pi*R

d = ((R+h)**2-R**2)**0.5
abertura = 60
def vecangle(r, theta):
    x = r*math.cos(theta/180*math.pi)
    y = r*math.sin(theta/180*math.pi)
    return np.array([x, y])

v1 = vecangle(d, 0)
v2 = vecangle(d, abertura)
dist = v1 - v2
p_dist = (dist[0]**2 + dist[1]**2)**.5
print('perimetro visto', p_dist)
print('em proporcao com o comprimento total aproximado: ', p_dist/C*100,'%')
print('em graus de curvatura: ', 360*p_dist/C, ' graus')

# 
# aqui e um dado da altura media do ser humano, 
# vamos agora fazer o caminho inverso
#
angulo = 1
h = R*((1+math.pi**2*angulo**2/(180**2*(2-2*math.cos(abertura))**0.5-1)
print('%f' % h)

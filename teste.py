import numpy as np
from math import *


R = 6356.6e+3
h = 1.70
C = 2*pi*R

d = ((R+h)**2-R**2)**0.5
distPrint = d/1000
print('distancia: %.4f' % distPrint)

alpha = asin(d/(R+h))*180/pi
print('angulo de visao: %.4fº' % alpha)

alpha = 1
alpha *=pi/180
h = R*cos(alpha)**(-1) - R
print('se ', alpha*180/pi, 'º,  h = ', h/1000, 'km')

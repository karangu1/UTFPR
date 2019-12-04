from math import *
import numpy as np
from cmath import *


def serie(vec):
    zeq = 0
    for valor in vec:
        zeq += valor
    return zeq

def paralelo(vec):
    zeq = 0
    for valor in vec:
        zeq += valor**(-1)
    return zeq**(-1)

fator = pi/180
a = complex(rect(1,120*fator))

mat1 = [1, 1, 1]
mat2 = [1, a**2, a]
mat3 = [1, a, a**2]
T = np.array([mat1, mat2, mat3])

print(T)

print()

from math import *
from cmath import *
print(abs(110.7 + 21.1j))

r = 0.099
xl = .518

Z = (r+xl*1j)*236

Va = rect(238,-15*pi/180)
print(Va)
Vb = rect(230,0)
print(Vb)

# A potencia na linha é dada por

S = (abs(Vb) - abs(Va))**2/Z
print('impedancia cabo :   ', Z)

# Calculo da corrente

I = (Vb-Va)/Z
print(I)
print("potencia dissipada na transmissao: ", abs(I*(Va-Vb)))
print('potencia A(kVA):  ', abs(I*Va))
print('potencia B(kVA):  ', abs(I*Vb))


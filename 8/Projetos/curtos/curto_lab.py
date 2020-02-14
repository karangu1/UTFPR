from math import *
from math import *
from cmath import *
import numpy as np

def paralelo(vec):
    resultado = 0
    for valor in vec:
        resultado += 1/valor
    return 1/resultado

def serie(vec):
    resultado = 0
    for valor in vec:
        resultado += valor
    return resultado

a = rect(1, 120*pi/180)
matriz = np.array([[1,1,1], [1,a**2,a], [1,a,a**2]])
#Declara??o dos dados de entrada#
Z1=0.7333+1.9560j               #Imped?ncia da rede (PU)#
Z0=1.2572+4.6321j               #Imped?ncia da rede (PU)#

Z1mt=0.987+0.348j               #Imped?ncia seq+ unit?ria cabo de MT (ohms/Km)#
Z0mt=0.987+0.348j               #Imped?ncia seq0 unit?ria cabo de MT (ohms/Km)#
dmt=377                         #Dist?ncia alimentador MT (m)#

#-----------------------------------------------------------------------
#QDG_6
Z1bt1=0.12+0.1381j              #Imped?ncia seq+ unit?ria cabo de BT1 QDG_1 (ohms/Km)#
Z0bt1=0.81+1.0048j              #Imped?ncia seq0 unit?ria cabo de BT1 (ohms/Km)#
dbt1=11                         #Dist?ncia alimentador BT1 (m)#
Nbt1=1                          #Quantia de cabos por fase alimentador BT1#

#CCM8
Z1bt2=0.87+0.2081j              #Imped?ncia seq+ unit?ria cabo de BT2 CCM1(ohms/Km)#
Z0bt2=5.01+1.2848j              #Imped?ncia seq0 unit?ria cabo de BT2 (ohms/Km)#
dbt2=17                         #Dist?ncia alimentador BT2 (m)#
Nbt2=1                          #Quantia de cabos por fase alimentador BT2#

#QDNB
Z1bt3=1.38+0.2281j              
Z0bt3=5.52+1.3048j              
dbt3=14                         
Nbt3=1  

#QD12
Z1bt4=0.32+0.1781j              
Z0bt4=2.21+1.1648j              
dbt4=27                         
Nbt4=1 

St=225                          #Potencia nominal do transformador (KVA)#
Pt=1000                         #Perdas no cobre do transformador (W)#
Zt=5                            #Impedancia do transformador (#)#
VnMT=13800                      #Tensao nominal do transformador - lado de MT (V)#
VnBT=380                        #Tensao nominal do transformador - lado de BT (V)#

#Declara??o das bases#
Sb=100e6
Vbmt=VnMT
Vbbt=VnBT
Ibmt=Sb/(sqrt(3)*Vbmt)
Zbmt=(Vbmt**2)/Sb
Ibbt=Sb/(sqrt(3)*Vbbt)
Zbbt=(Vbbt**2)/Sb
a=1*exp(120*pi/180*(0+1j))

#--------------------------------------
Zaterpu = (1.65+0j)/Zbbt
#--------------------------------------

#Imped?ncia dos alimetadores MT em PU#
Z1mtpu=(Z1mt*dmt*0.001)/Zbmt
Z0mtpu=(Z0mt*dmt*0.001)/Zbmt

#Imped?ncia dos alimetadores BT em PU#
Z1bt1pu=(Z1bt1*dbt1*0.001/Nbt1)/Zbbt
Z0bt1pu=(Z0bt1*dbt1*0.001/Nbt1)/Zbbt

Z1bt2pu=(Z1bt2*dbt2*0.001/Nbt2)/Zbbt
Z0bt2pu=(Z0bt2*dbt2*0.001/Nbt2)/Zbbt

Z1bt3pu=(Z1bt3*dbt3*0.001/Nbt3)/Zbbt
Z0bt3pu=(Z0bt3*dbt3*0.001/Nbt3)/Zbbt

Z1bt4pu=(Z1bt4*dbt4*0.001/Nbt4)/Zbbt
Z0bt4pu=(Z0bt4*dbt4*0.001/Nbt4)/Zbbt

#Imped?ncia do transformador
Rt=Pt/(St*1000)
Xlt=sqrt(((Zt/100)**2)-(Rt**2))
Zt=(Rt+Xlt*(0+1j))*(Sb/(St*1000))

#  Gerador 
xd = 16.34/100
Zg1 = xd*(Sb/295e+3)
Zg2 = Zg1/2
Zg0 = 0.5*Zg1
Zterra = 0.55 + 0j

# ********************************************************
# ********************************************************
# ********************************************************
# ********************************************************
# ************ CALCULO DOS CURTO CIRCUITOS ***************
# ********************************************************
# ********************************************************
# ********************************************************
# ********************************************************

# CC 3f no gerador
Ia1 = 1/Zg1
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("CC 3f no gerador:  ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC 3f no ccm8

Ia1 = 1/serie([Zg1, Z1bt2pu])
Ia1 = Ia1*Ibbt 
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("CC 3f no ccm8:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC 3f no qdnb

Ia1 = 1/serie([Zg1, Z1bt3pu])
Ia1 = Ia1*Ibbt 
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("# CC 3f no qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC 3f no qd12

Ia1 = 1/serie([Zg1, Z1bt4pu])
Ia1 = Ia1*Ibbt 
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("# CC 3f no qd12:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# --------------
# CC monofasico
# gerador

Ia1 = 1/serie([Zg1, Zg2, Zg0, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC monofasico
# Cargas
# CCM8

Ia1 = 1/serie([Zg1, Zg2, Zg0, Z1bt2pu, Z1bt2pu, Z0bt2pu, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no ccm8:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# QDNB

Ia1 = 1/serie([Zg1, Zg2, Zg0, Z1bt3pu, Z1bt3pu, Z0bt3pu, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# QD12

Ia1 = 1/serie([Zg1, Zg2, Zg0, Z1bt4pu, Z1bt4pu, Z0bt4pu, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no qd12:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# --------------
# CC Bifásico
# gerador

Ia1 = 1/serie([Zg1, Zg2])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# Cargas
# ccm8
Ia1 = 1/serie([Zg1, Zg2, Z1bt2pu, Z1bt2pu])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qdnb
Ia1 = 1/serie([Zg1, Zg2, Z1bt3pu, Z1bt3pu])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qd12
Ia1 = 1/serie([Zg1, Zg2, Z1bt4pu, Z1bt4pu])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# --------------
# CC Bifásico aterrado
# gerador

Ia1 = 1/(Zg1+paralelo([Zg2,Zg0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([Zg2,Zg0])/Zg2
Ia0 = -Ia1*paralelo([Zg2,Zg0])/Zg0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2ft no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# Cargas
# CCM8
seq2 = Zg2 + Z1bt2pu
seq0 = Zg0 + Z0bt2pu + Zterra
Ia1 = 1/(Zg1 + Z1bt2pu + paralelo([seq2,seq0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([seq2,seq0])/seq2
Ia0 = -Ia1*paralelo([seq2,seq0])/seq0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2ft ccm8:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qdnb

seq2 = Zg2 + Z1bt3pu
seq0 = Zg0 + Z0bt3pu + Zterra
Ia1 = 1/(Zg1 + Z1bt3pu + paralelo([seq2,seq0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([seq2,seq0])/seq2
Ia0 = -Ia1*paralelo([seq2,seq0])/seq0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2f qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qd12

seq2 = Zg2 + Z1bt4pu
seq0 = Zg0 + Z0bt4pu + Zterra
Ia1 = 1/(Zg1 + Z1bt4pu + paralelo([seq2,seq0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([seq2,seq0])/seq2
Ia0 = -Ia1*paralelo([seq2,seq0])/seq0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2f qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))









from cmath import *
import numpy as np

def paralelo(vec):
    resultado = 0
    for valor in vec:
        resultado += 1/valor
    return 1/resultado

def serie(vec):
    resultado = 0
    for valor in vec:
        resultado += valor
    return resultado

a = rect(1, 120*pi/180)
matriz = np.array([[1,1,1], [1,a**2,a], [1,a,a**2]])
#Declara??o dos dados de entrada#
Z1=0.7333+1.9560j               #Imped?ncia da rede (PU)#
Z0=1.2572+4.6321j               #Imped?ncia da rede (PU)#

Z1mt=0.987+0.348j               #Imped?ncia seq+ unit?ria cabo de MT (ohms/Km)#
Z0mt=0.987+0.348j               #Imped?ncia seq0 unit?ria cabo de MT (ohms/Km)#
dmt=377                         #Dist?ncia alimentador MT (m)#

#-----------------------------------------------------------------------
#QDG_6
Z1bt1=0.12+0.1381j              #Imped?ncia seq+ unit?ria cabo de BT1 QDG_1 (ohms/Km)#
Z0bt1=0.81+1.0048j              #Imped?ncia seq0 unit?ria cabo de BT1 (ohms/Km)#
dbt1=11                         #Dist?ncia alimentador BT1 (m)#
Nbt1=1                          #Quantia de cabos por fase alimentador BT1#

#CCM8
Z1bt2=0.87+0.2081j              #Imped?ncia seq+ unit?ria cabo de BT2 CCM1(ohms/Km)#
Z0bt2=5.01+1.2848j              #Imped?ncia seq0 unit?ria cabo de BT2 (ohms/Km)#
dbt2=17                         #Dist?ncia alimentador BT2 (m)#
Nbt2=1                          #Quantia de cabos por fase alimentador BT2#

#QDNB
Z1bt3=1.38+0.2281j              
Z0bt3=5.52+1.3048j              
dbt3=14                         
Nbt3=1  

#QD12
Z1bt4=0.32+0.1781j              
Z0bt4=2.21+1.1648j              
dbt4=27                         
Nbt4=1 

St=225                          #Potencia nominal do transformador (KVA)#
Pt=1000                         #Perdas no cobre do transformador (W)#
Zt=5                            #Impedancia do transformador (#)#
VnMT=13800                      #Tensao nominal do transformador - lado de MT (V)#
VnBT=380                        #Tensao nominal do transformador - lado de BT (V)#

#Declara??o das bases#
Sb=100e6
Vbmt=VnMT
Vbbt=VnBT
Ibmt=Sb/(sqrt(3)*Vbmt)
Zbmt=(Vbmt**2)/Sb
Ibbt=Sb/(sqrt(3)*Vbbt)
Zbbt=(Vbbt**2)/Sb
a=1*exp(120*pi/180*(0+1j))

#--------------------------------------
Zaterpu = (1.65+0j)/Zbbt
#--------------------------------------

#Imped?ncia dos alimetadores MT em PU#
Z1mtpu=(Z1mt*dmt*0.001)/Zbmt
Z0mtpu=(Z0mt*dmt*0.001)/Zbmt

#Imped?ncia dos alimetadores BT em PU#
Z1bt1pu=(Z1bt1*dbt1*0.001/Nbt1)/Zbbt
Z0bt1pu=(Z0bt1*dbt1*0.001/Nbt1)/Zbbt

Z1bt2pu=(Z1bt2*dbt2*0.001/Nbt2)/Zbbt
Z0bt2pu=(Z0bt2*dbt2*0.001/Nbt2)/Zbbt

Z1bt3pu=(Z1bt3*dbt3*0.001/Nbt3)/Zbbt
Z0bt3pu=(Z0bt3*dbt3*0.001/Nbt3)/Zbbt

Z1bt4pu=(Z1bt4*dbt4*0.001/Nbt4)/Zbbt
Z0bt4pu=(Z0bt4*dbt4*0.001/Nbt4)/Zbbt

#Imped?ncia do transformador
Rt=Pt/(St*1000)
Xlt=sqrt(((Zt/100)**2)-(Rt**2))
Zt=(Rt+Xlt*(0+1j))*(Sb/(St*1000))

#  Gerador 
xd = 16.34/100
Zg1 = xd*(Sb/295e+3)
Zg2 = Zg1/2
Zg0 = 0.5*Zg1
Zterra = 0.55 + 0j

# ********************************************************
# ********************************************************
# ********************************************************
# ********************************************************
# ************ CALCULO DOS CURTO CIRCUITOS ***************
# ********************************************************
# ********************************************************
# ********************************************************
# ********************************************************

# CC 3f no gerador
Ia1 = 1/Zg1
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("CC 3f no gerador:  ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC 3f no ccm8

Ia1 = 1/serie([Zg1, Z1bt2pu])
Ia1 = Ia1*Ibbt 
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("CC 3f no ccm8:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC 3f no qdnb

Ia1 = 1/serie([Zg1, Z1bt3pu])
Ia1 = Ia1*Ibbt 
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("# CC 3f no qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC 3f no qd12

Ia1 = 1/serie([Zg1, Z1bt4pu])
Ia1 = Ia1*Ibbt 
[Ia, Ib, Ic] = matriz.dot([Ia1,0,0])
print("# CC 3f no qd12:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# --------------
# CC monofasico
# gerador

Ia1 = 1/serie([Zg1, Zg2, Zg0, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# CC monofasico
# Cargas
# CCM8

Ia1 = 1/serie([Zg1, Zg2, Zg0, Z1bt2pu, Z1bt2pu, Z0bt2pu, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no ccm8:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# QDNB

Ia1 = 1/serie([Zg1, Zg2, Zg0, Z1bt3pu, Z1bt3pu, Z0bt3pu, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# QD12

Ia1 = 1/serie([Zg1, Zg2, Zg0, Z1bt4pu, Z1bt4pu, Z0bt4pu, Zterra])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia1,Ia1])
print("# CC 1f no qd12:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# --------------
# CC Bifásico
# gerador

Ia1 = 1/serie([Zg1, Zg2])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# Cargas
# ccm8
Ia1 = 1/serie([Zg1, Zg2, Z1bt2pu, Z1bt2pu])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qdnb
Ia1 = 1/serie([Zg1, Zg2, Z1bt3pu, Z1bt3pu])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qd12
Ia1 = 1/serie([Zg1, Zg2, Z1bt4pu, Z1bt4pu])
Ia1 = Ia1*Ibbt
[Ia, Ib, Ic] = matriz.dot([Ia1,-Ia1,0])
print("# CC 2f no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# --------------
# CC Bifásico aterrado
# gerador

Ia1 = 1/(Zg1+paralelo([Zg2,Zg0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([Zg2,Zg0])/Zg2
Ia0 = -Ia1*paralelo([Zg2,Zg0])/Zg0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2ft no gerador:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# Cargas
# CCM8
seq2 = Zg2 + Z1bt2pu
seq0 = Zg0 + Z0bt2pu + Zterra
Ia1 = 1/(Zg1 + Z1bt2pu + paralelo([seq2,seq0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([seq2,seq0])/seq2
Ia0 = -Ia1*paralelo([seq2,seq0])/seq0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2ft ccm8:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qdnb

seq2 = Zg2 + Z1bt3pu
seq0 = Zg0 + Z0bt3pu + Zterra
Ia1 = 1/(Zg1 + Z1bt3pu + paralelo([seq2,seq0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([seq2,seq0])/seq2
Ia0 = -Ia1*paralelo([seq2,seq0])/seq0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2f qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))

# qd12

seq2 = Zg2 + Z1bt4pu
seq0 = Zg0 + Z0bt4pu + Zterra
Ia1 = 1/(Zg1 + Z1bt4pu + paralelo([seq2,seq0]))
Ia1 = Ia1*Ibbt
Ia2 = -Ia1*paralelo([seq2,seq0])/seq2
Ia0 = -Ia1*paralelo([seq2,seq0])/seq0
[Ia, Ib, Ic] = matriz.dot([Ia1,Ia2,Ia0])
print("# CC 2f qdnb:   ")
print("%.4f" % abs(Ia))
print("%.4f" % abs(Ib))
print("%.4f" % abs(Ic))










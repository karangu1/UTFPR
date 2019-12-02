clear all
format short
clc

%Declaração dos dados de entrada%
Z1=0.7333+1.9560i               %Impedância da rede (PU)%
Z0=1.2572+4.6321i               %Impedância da rede (PU)%

Z1mt=0.987+0.348i               %Impedância seq+ unitária cabo de MT (ohms/Km)%
Z0mt=0.987+0.348i               %Impedância seq0 unitária cabo de MT (ohms/Km)%
dmt=377                         %Distância alimentador MT (m)%

%-----------------------------------------------------------------------
%QDG_6
Z1bt1=0.12+0.1381i              %Impedância seq+ unitária cabo de BT1 QDG_1 (ohms/Km)%
Z0bt1=0.81+1.0048i              %Impedância seq0 unitária cabo de BT1 (ohms/Km)%
dbt1=11                         %Distância alimentador BT1 (m)%
Nbt1=1                          %Quantia de cabos por fase alimentador BT1%

%CCM8
Z1bt2=0.87+0.2081i              %Impedância seq+ unitária cabo de BT2 CCM1(ohms/Km)%
Z0bt2=5.01+1.2848i              %Impedância seq0 unitária cabo de BT2 (ohms/Km)%
dbt2=17                         %Distância alimentador BT2 (m)%
Nbt2=1                          %Quantia de cabos por fase alimentador BT2%

%QDNB
Z1bt3=1.38+0.2281i              
Z0bt3=5.52+1.3048i              
dbt3=14                         
Nbt3=1  

%QD12
Z1bt4=0.32+0.1781i              
Z0bt4=2.21+1.1648i              
dbt4=27                         
Nbt4=1 

St=225                          %Potência nominal do transformador (KVA)%
Pt=1000                         %Perdas no cobre do transformador (W)%
Zt=5                            %Impedância do transformador (%)%
VnMT=13800                      %Tensão nominal do transformador - lado de MT (V)%
VnBT=380                        %Tensão nominal do transformador - lado de BT (V)%

%Declaração das bases%
Sb=100e6
Vbmt=VnMT
Vbbt=VnBT
Ibmt=Sb/(sqrt(3)*Vbmt)
Zbmt=(Vbmt^2)/Sb
Ibbt=Sb/(sqrt(3)*Vbbt)
Zbbt=(Vbbt^2)/Sb
a=1*exp(120*pi/180*1i)

%--------------------------------------
Zaterpu = (1.65+0i)/Zbbt
%--------------------------------------

%Impedância dos alimetadores MT em PU%
Z1mtpu=(Z1mt*dmt*0.001)/Zbmt
Z0mtpu=(Z0mt*dmt*0.001)/Zbmt

%Impedância dos alimetadores BT em PU%
Z1bt1pu=(Z1bt1*dbt1*0.001/Nbt1)/Zbbt
Z0bt1pu=(Z0bt1*dbt1*0.001/Nbt1)/Zbbt

Z1bt2pu=(Z1bt2*dbt2*0.001/Nbt2)/Zbbt
Z0bt2pu=(Z0bt2*dbt2*0.001/Nbt2)/Zbbt

Z1bt3pu=(Z1bt3*dbt3*0.001/Nbt3)/Zbbt
Z0bt3pu=(Z0bt3*dbt3*0.001/Nbt3)/Zbbt

Z1bt4pu=(Z1bt4*dbt4*0.001/Nbt4)/Zbbt
Z0bt4pu=(Z0bt4*dbt4*0.001/Nbt4)/Zbbt

%Impedância do transformador
Rt=Pt/(St*1000)
Xlt=sqrt(((Zt/100)^2)-(Rt^2))
Zt=(Rt+Xlt*1i)*(Sb/(St*1000))

%Cálculo das Correntes de Curto-Circuito trifásica%
%Ponto de Entrega%
Ia1=1/Z1
Icc3fPe=Ia1*Ibmt

%Primário Transformador%
Ia1=1/(Z1+Z1mtpu)
Icc3fPT1=Ia1*Ibmt

%Secundário Transformador%
Ia1=1/(Z1+Z1mtpu+Zt)
Icc3fST1=Ia1*Ibbt

%QDG6%
Ia1=1/(Z1+Z1mtpu+Zt+Z1bt1pu)
Icc3fQDG6=Ia1*Ibbt

%CCM8%
Ia1=1/(Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt2pu)
Icc3fCCM8=Ia1*Ibbt

%QDNB%
Ia1=1/(Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt3pu)
Icc3fQDNB=Ia1*Ibbt

%QD12%
Ia1=1/(Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt4pu)
Icc3fQD12=Ia1*Ibbt

%Cálculo das Correntes de Curto-Circuito bifásica%
k=sqrt(3)*exp(-(pi/2)*1i)

%Ponto de Entrega%
Ia1=1/(2*Z1)
Icc2fPe=k*Ia1*Ibmt

%Primário Transformador%
Ia1=1/(2*(Z1+Z1mtpu))
Icc2fPT1=k*Ia1*Ibmt

%Secundário Transformador%
Ia1=1/(2*(Z1+Z1mtpu+Zt))
Icc2fST1=k*Ia1*Ibbt

%QDG6%
Ia1=1/(2*(Z1+Z1mtpu+Zt+Z1bt1pu))
Icc2fQDG6=k*Ia1*Ibbt

%CCM8%
Ia1=1/(2*(Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt2pu))
Icc2fCCM8=k*Ia1*Ibbt

%QDNB%
Ia1=1/(2*(Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt3pu))
Icc2fQDNB=k*Ia1*Ibbt

%QD12%
Ia1=1/(2*(Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt4pu))
Icc2fQD12=k*Ia1*Ibbt

%Cálculo das Correntes de Curto-Circuito fase-fase-terra%
%Ponto de Entrega%
R1=Z1
R2=R1
R0=Z0
Req=(R2*R0)/(R2+R0)
Ia1=1/(R1+Req)
Ia2=(1*exp(pi*1i))*Ia1*Req/R2
Ia0=(1*exp(pi*1i))*Ia1*Req/R0
Icc2ftPe=(Ia0+(Ia1*a^2)+(a*Ia2))*Ibmt

%Primário Transformador%
R1=Z1+Z1mtpu
R2=R1
R0=Z0+Z0mtpu
Req=(R2*R0)/(R2+R0)
Ia1=1/(R1+Req)
Ia2=(1*exp(pi*1i))*Ia1*Req/R2
Ia0=(1*exp(pi*1i))*Ia1*Req/R0
Icc2ftPT1=(Ia0+(Ia1*a^2)+(a*Ia2))*Ibmt


%Secundário Transformador%
R1=Z1+Z1mtpu+Zt
R2=R1
R0=0.85*Zt
Req=(R2*R0)/(R2+R0)
Ia1=1/(R1+Req)
Ia2=(1*exp(pi*1i))*Ia1*Req/R2
Ia0=(1*exp(pi*1i))*Ia1*Req/R0
Icc2ftST1=(Ia0+(Ia1*a^2)+(a*Ia2))*Ibbt


%QDG6%
R1=Z1+Z1mtpu+Zt+Z1bt1pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Zaterpu
Req=(R2*R0)/(R2+R0)
Ia1=1/(R1+Req)
Ia2=(1*exp(pi*1i))*Ia1*Req/R2
Ia0=(1*exp(pi*1i))*Ia1*Req/R0
Icc2ftQDG6=(Ia0+(Ia1*a^2)+(a*Ia2))*Ibbt

%CCM8%
R1=Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt2pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Z0bt2pu+Zaterpu
Req=(R2*R0)/(R2+R0)
Ia1=1/(R1+Req)
Ia2=(1*exp(pi*1i))*Ia1*Req/R2
Ia0=(1*exp(pi*1i))*Ia1*Req/R0
Icc2ftCCM8=(Ia0+(Ia1*a^2)+(a*Ia2))*Ibbt

%QDNB%
R1=Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt3pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Z0bt3pu+Zaterpu
Req=(R2*R0)/(R2+R0)
Ia1=1/(R1+Req)
Ia2=(1*exp(pi*1i))*Ia1*Req/R2
Ia0=(1*exp(pi*1i))*Ia1*Req/R0
Icc2ftQDNB=(Ia0+(Ia1*a^2)+(a*Ia2))*Ibbt

%QD12%
R1=Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt4pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Z0bt4pu+Zaterpu
Req=(R2*R0)/(R2+R0)
Ia1=1/(R1+Req)
Ia2=(1*exp(pi*1i))*Ia1*Req/R2
Ia0=(1*exp(pi*1i))*Ia1*Req/R0
Icc2ftQD12=(Ia0+(Ia1*a^2)+(a*Ia2))*Ibbt


%Cálculo das Correntes de Curto-Circuito fase-terra%

%Ponto de Entrega%
R1=Z1
R2=R1
R0=Z0
Ia0=1/(R1+R2+R0)
Ia1=Ia0
Ia2=Ia0
Icc1fPe=3*Ia0*Ibmt

%Primário Transformador%
R1=Z1+Z1mtpu
R2=R1
R0=Z0+Z0mtpu
Ia0=1/(R1+R2+R0)
Ia1=Ia0
Ia2=Ia0
Icc1fPT1=3*Ia0*Ibmt

%Secundário Transformador%
R1=Z1+Z1mtpu+Zt
R2=R1
R0=0.85*Zt
Ia0=1/(R1+R2+R0)
Ia1=Ia0
Ia2=Ia0
Icc1fST1=3*Ia0*Ibbt
Va1=1-(R1*Ia1)
Va2=R2*-Ia2
Va0=R0*-Ia0
Va=(Va0+Va1+Va2)*Vbbt
Vb=(Va0+(Va1*a^2)+(Va2*a))*Vbbt
Vc=(Va0+(Va1*a)+(Va2*a^2))*Vbbt

%QDG6%
R1=Z1+Z1mtpu+Zt+Z1bt1pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Zaterpu
Ia0=1/(R1+R2+R0)
Ia1=Ia0
Ia2=Ia0
Icc1fQDG6=3*Ia0*Ibbt

%CCM8%
R1=Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt2pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Z0bt2pu+Zaterpu
Ia0=1/(R1+R2+R0)
Ia1=Ia0
Ia2=Ia0
Icc1fCCM8=3*Ia0*Ibbt

%QDNB%
R1=Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt3pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Z0bt3pu+Zaterpu
Ia0=1/(R1+R2+R0)
Ia1=Ia0
Ia2=Ia0
Icc1fQDNB=3*Ia0*Ibbt

%QD12%
R1=Z1+Z1mtpu+Zt+Z1bt1pu+Z1bt4pu
R2=R1
R0=(0.85*Zt)+Z0bt1pu+Z0bt4pu+Zaterpu
Ia0=1/(R1+R2+R0)
Ia1=Ia0
Ia2=Ia0
Icc1fQD12=3*Ia0*Ibbt

%Apresentação correntes%
Icc3f=[abs(Icc3fPe); abs(Icc3fPT1); abs(Icc3fST1); abs(Icc3fQDG6); abs(Icc3fCCM8); abs(Icc3fQDNB); abs(Icc3fQD12)]
Icc2f=[abs(Icc2fPe); abs(Icc2fPT1); abs(Icc2fST1); abs(Icc2fQDG6); abs(Icc2fCCM8); abs(Icc2fQDNB); abs(Icc2fQD12)]
Icc2ft=[abs(Icc2ftPe); abs(Icc2ftPT1); abs(Icc2ftST1); abs(Icc2ftQDG6); abs(Icc2ftCCM8); abs(Icc2ftQDNB); abs(Icc2ftQD12)]
Icc1f=[abs(Icc1fPe); abs(Icc1fPT1); abs(Icc1fST1); abs(Icc1fQDG6); abs(Icc1fCCM8); abs(Icc1fQDNB); abs(Icc1fQD12)]
format bank
Pontos={'Pe';'Tr_Pri';'Tr_Sec';'QDG6';'CCM8';'QDNB';'QD12'}
clc
T=table(Icc3f,Icc2f,Icc2ft,Icc1f,'RowNames',Pontos)
format short

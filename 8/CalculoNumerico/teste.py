import math

e=math.e
# e**(2*x)-e**x-2
# 2*e**(2*x)-e**x

print("A express�o � colocada dentro do script, este programa � s� para rodar diferentes m�todos")
# print("Escolha o m�todo:")
print("(1)   Secante")
print("(2)   Tangente")
# print("(3)   Bissec��o")
# print("(4)   Falsa posi��o")
b=input()



if(b == str(1)):
    # Funções
    x       = float(input("x1:"))
    x1      = float(input("x2:"))
    i       = int(input("itera�oes:"))
    for a in range(1,i+1):
        f1  = e**(2*x1)-e**x1-2
        f   = e**(2*x)-e**x-2
        x2  = x1 - f1*(x1-x)/(f1-f)
        print(str(a)+"     "+str(x)+"   "+str(x1)+"    "+str(x2)+"    "+str(f)+"    "+str(f1)+"   ")
        x   = x1
        x1  = x2
elif(b==str(2)):
    x       = float(input("x1:"))
    i       = int(input("itera�oes:"))
    for a in range(1, i+1):
        f       = e**(2*x)-e**x-2
        fder    = 2*e**(2*x)-e**x
        xnext = x - f/fder
        print(str(a) + "    " + str(x) + "    " + str(xnext) + "   " + str(f) + "    " + str(fder))
        x = xnext

input("\n\n\nPressione Enter para sair")

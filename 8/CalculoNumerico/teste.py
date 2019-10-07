import math

e=math.e
# e**(2*x)-e**x-2
# 2*e**(2*x)-e**x

print("A expressao e colocada dentro do script, este programa e so para rodar diferentes metodos")
# print("Escolha o metodo:")
print("(1)   Secante")
print("(2)   Tangente")
print("Outro Funcao")
# print("(3)   Bisseccao")
# print("(4)   Falsa posicao")
b=input()



if(b == str(1)):
    # Funções
    x       = float(input("x1:"))
    x1      = float(input("x2:"))
    i       = int(input("itera?oes:"))
    for a in range(1,i+1):
        f1  = e**(2*x1)-e**x1-2
        f   = e**(2*x)-e**x-2
        x2  = x1 - f1*(x1-x)/(f1-f)
        print("%.0f %.4f  %.4f  %.4f  %.4f   %.4f " % (a, x, x1, x2 , f, f1))
        x   = x1
        x1  = x2
elif(b==str(2)):
    x       = float(input("x1:"))
    i       = int(input("itera?oes:"))
    print('i x_i     x_i+1     f        f`')
    for a in range(1, i+1):
        f       = e**(2*x)-e**x-2
        fder    = 2*e**(2*x)-e**x
        xnext = x - f/fder
        print("%.0f %.4f  %.4f  %.4f  %.4f " % (a, x, xnext, f , fder))
        x = xnext
else:
    x = input('x=')
    print('Ainda nao temos suporte para funcao digitada')


input("\n\n\nPressione Enter para sair")

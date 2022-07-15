#2. Considere o programa a seguir.
def f1(a,b): #retorna o menor
    if a>b:
        return b
    else:
        return a
def f2(a,b,c):
    x = f1(b,c) #x=15 x=10
    y = x+f1(c,a) #y=10 y=20
    return x+y
x,y,z = map(int,input().split())
print(f2(x,y,z))
#Escreva a saída do programa para os valores de entrada:
#• 10, 20 e 15 - 25
#• 20, 10 e 30 - 30
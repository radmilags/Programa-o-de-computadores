#1. Seja o programa a seguir.
def f1(a,b):
    return a*2+b*3
x,y = map(int,input().split())
print(f1(10,20)) #80
print(f1(x,10))
print(f1(20,y))
print(f1(x,y))
#Escreva a saída do programa para os valores de entrada:
#• 100 e 200 - 230, 640 e 800
#• 10 e 20 - 50, 100 e 80
#• 2 e 3 - 34, 49, 13

'''9. A função de potenciação a
e pode ser escrita como a × a
e−1 para todo valor de
e maior-igual a 1. Para e igual a zero a função retorna 1. Esta propriedade
pode ser descrita como na equação a seguir.
a
e =
{
1 se e = 0
a × a
e−1
senão
Escreva um programa que leia 2 (dois) números inteiros não negativos a e e da
entrada padrão e escreva o valor de a
e na saída padrão.
Exemplo de entrada e saída para a execução do programa:'''

def mul(a, e):
    if e == 0: return 1
    if e == 1: return a
    return #corrigir

a, e = map(int,input().split())
print(mul(a, e))

'''
a**5 = a*a**4
a**4 = a*a**3
a**3 = a*a**2
a**2 = a*a**1
a**1 = a*a**0
a**0 = 1
'''
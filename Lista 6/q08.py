'''8. Escreva um programa que leia dois números inteiros não negativos e mostre a
soma dos fatoriais do mesmo 4
.
Escreva uma função recursiva para calcular o fatorial de um número.
Exemplo de entrada e saída para a execução do programa:'''
def fatorial(a):
    if a == 0: return 1
    return a*fatorial(a-1)
a, b = map(int,input().split())
print(fatorial(a)+fatorial(b))
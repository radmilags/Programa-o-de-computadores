print("9. Escreva um programa que leia uma lista de números inteiros e mostre se a soma dos números é par ou ímpar. Exemplo de entrada e saída para a execução do programa:")
s = list(map(int, input().split()))
if sum(s)%2 == 0: print("Par")
else: print("Ímpar")
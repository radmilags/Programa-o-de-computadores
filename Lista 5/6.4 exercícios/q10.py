print("10. Escreva um programa que leia uma lista de números inteiros e mostre se a soma dos números é divisível pela quantidade de números lidos.")
s = list(map(int, input().split()))
if sum(s)%len(s) == 0: print("Sim")
else: print("Nao")
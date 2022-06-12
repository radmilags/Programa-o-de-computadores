print("8. Escreva um programa que leia uma lista de números inteiros e mostre o menor número e o maior número da lista.")
s = list(map(int, input().split()))
s.sort()
print(s[0], s[len(s)-1])
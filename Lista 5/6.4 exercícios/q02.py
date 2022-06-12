print("2. Escreva um programa que leia uma lista de números e troque o primeiro elemento com o segundo. Depois mostre a nova lista. Exemplo de entrada e saída para a execução do programa:")
s = list(input().split())
aux = s[0]
s[0] = s[1]
s[1] = aux
print(s)
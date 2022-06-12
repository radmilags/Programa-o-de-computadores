print("4. Escreva um programa que leia uma lista de 8 números e troque de lugar o primeiro número e o último número. Mostre a lista modificada. Exemplo de entrada e saída para a execução do programa:")
s = list(input().split())
aux = s[0]
s[0] = s[7]
s[7] = aux
print(s)
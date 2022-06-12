from re import X


print("5. Escreva um programa que leia um lista de números inteiros em uma linha, depois leia um número inteiro e adicione o número lido ao final da lista. Mostre A nova lista na tela Exemplo de entrada e saída para a execução do programa:")
s = list(map(int, input().split()))
s.append(int(input()))
print(s)
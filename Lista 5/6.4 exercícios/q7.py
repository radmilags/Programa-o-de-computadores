print("7. Escreva um programa que leia uma lista de números, separados por espaço, mostre a quantidade de números lidos, o primeiro número e o último número da lista. Exemplo de entrada e saída para a execução do programa:")
s = list(map(int, input().split()))
print(len(s), s[0], s[len(s)-1])
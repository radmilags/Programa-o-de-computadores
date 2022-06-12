print("11. Escreva um programa que leia uma lista de números, separados por espaço, e mostre o número localizado no meio da lista. Caso a lista tenha uma quantidade par de números o programa mostra a média dos dois números do meio. Exemplo de entrada e saída para a execução do programa:")
s = list(map(int, input().split()))
if len(s)%2 == 0: print((s[(len(s)//2)-1]+s[len(s)//2])/2)
else: print(s[len(s)//2])
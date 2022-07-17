'''10. Escreva um programa que leia um número inteiro não negativo e escreva a
quantidade de vezes que cada dígito ocorre no número. Escreva um função
recursiva para contar a quantidade de ocorrência de um dígito d em um número
n A assinatura da função é:''' #é isso que o problema pede

def conta_digitos(n,d): #numero que eu vou receber
    count = 0 
    for i in range(len(n)):
        if n[i] == d: count += 1
    return print(count)
n = input()
d = input()
count = 0 
conta_digitos(n, d)

def contador(n):
    i = 0
    count = 0 
    while i < 9:
        for j in range(len(n)):
            if n[j] == d: count += 1
            return print(i, ":", count)
        count = 0

n = input()


# 1. Escreva um programa que escreva na tela a seguinte mensagem:
print("Meu primeiro programa!")

# 2. Escreva um programa que escreva na tela o endereço do IFRN da seguinte forma:
print("Avenida Senador Salgado Filho, 1559,")
print("Tirol, Natal-RN, Brasil")
print("CEP: 59015-000")
print("e-mail: ccs.cnat@ifrn.edu.br")
print("Telefone: 4005-2600")

# 3. Escreva um programa que leia seu nome e mostre a seguinte mensagem:
s = input()
print("Oi", s, "bom dia!")

# 4. Escreva um programa que leia dois números inteiros e mostre a soma dos mesmos.
x = int(input())
y = int(input())
print(x+y)

# 5. Escreva um programa que leia dois números reais e mostre a média aritmética dos mesmos.
f1 = float(input())
f2 = float(input())
print((f1+f2)/2)

# 6. Escreva um programa que leia duas notas e mostre a média obtida a partir das mesmas, de acordo com as regras do IFRN.
x = int(input()) 
while x < 0 or x > 100:
    x = int(input()) 
y = int(input()) 
while y < 0 or y > 100:
    y = int(input())

print((x*2 + y*3) / 5)

# 7. Escreva um programa leia três (3) números e mostre o produto dos mesmos. Exemplo de entrada e saída para a execução do programa:
x = int(input())
y = int(input())
z = int(input())
print(x*y*z)

# 8. Escreva um programa que leia a hora de início e de fim de um evento e mostre o tempo do evento no formato HH:MM. 
# A hora de início e fim é dada em minutos desde o início do dia.
x = int(input())
y = int(input())
z = y - x
h1 = z // 60
m1 = z % 60
print(h1,":",m1)

# 9. Escreva um programa que leia a quantidade de dias desde o início do ano 
# e mostre quantas semanas e quantos dias já se passaram desde do dia primeiro de janeiro
x = int(input())
sem = x // 7
d = x % 7
print(sem, "semana(s)")
print(d, "dia(s)")

# 10. Escreva um programa que leia o valor de um item a venda, a quantidade de
# itens que você vai comprar e o valor que você tem para pagar. Todos os valores
# são inteiros. O programa deve então informar o valor total a ser pago e o valor
# do troco que você vai receber
x = int(input()) #valor item
y = int(input()) #quant itens
z = int(input()) #valor que pagou
v = x*y #valor a pagar
print("A pagar:", v)
print("Troco :", z - v)

# 11. Escreva um programa que leia a distância entre duas cidades A e B, em kilômetros, 
# a velocidade, em km/h, do carro e mostre qual o tempo da viagem entre
# A e B, no formato HH:MM. Os segundos devem ser desprezados.

distancia = int(input())
vel = int(input())
h = distancia // vel
min = ((distancia / vel)- h)*60
min = round(min)
print(h , ":", min)


# 12. Escreva um programa que calcule a quantidade de postes a serem colocados
# em uma rua. O programa deve ler a distância do início ao fim da rua, em
# quilômetros e a distância entre dois (2) postes, em metros. Seu programa
# deve mostrar a quantidade de postes e a distância entre os dois últimos postes.
# Lembre-se que há sempre um poste no início da rua e outro no final. A distância
# entre cada par de postes é o valor, em metros, lido pelo programa, com exceção
# da distância entre os dois últimos postes da rua.
# Exemplo de entrada e saída para a execução do programa:
from math import ceil
comprimento = float(input("digite o comprimento da rua em km: ")) * 1000

distancia = float(input("digite a distância entre os postes(em m): "))

quantidade = (comprimento / distancia) + 1
quant = ceil(quantidade)
ultimo = comprimento % distancia

print(f"a quantidade de postes vai ser de {quant}")
print(f"e a distância entre os dois ultimos vai ser de {ultimo} ")
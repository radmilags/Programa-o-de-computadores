print("1. Determine o valor e o tipo de x após a seguinte instrução ser executada")
x=10+3*3
print("x=10+3*3, x =",x)

print("2. Determine o valor e o tipo de x após a seguinte instrução ser executada.")
x=10+18/2
print("x=10+18/2, x =",x)

print("3. Determine o valor e o tipo de x após a seguinte instrução ser executada.")
x=10+18//2-1
print("x=10+18//2-1, x =",x)

print("4. Determine o valor e o tipo de x após a seguinte instrução ser executada. Qual o tipo do resultado e porque?")
x=1+2*3+40//3%5-2+3*5%2
print("x=1+2*3+40//3%5-2+3*5%2 , x =",x)

print("5. Determine o valor e o tipo de x após a seguinte instrução ser executada. Qual o tipo do resultado e porque?")
x=1+2*3+40/3%5-2+3//2*5
print("x=1+2*3+40/3%5-2+3//2*5 , x =",x)
 
print("6. Usando o interpretador Python3, calcule a soma dos números de 1 a 10, atribua a variável x e mostre seu valor.")
x = 1
x += 2
x += 3
x += 4
x += 5
x += 6
x += 7
x += 8
x += 9
x += 10
print("x=",x, ", tipo inteiro")

print("7. Usando o interpretador Python3, calcule a média aritmética entre 7, 7 e 8, 35, atribua a variável media e mostre seu valor.")
media = (7+7+8+35)/4
print("MEDIA =", media, ", tipo float")

print("8. Considere duas variáveis n1 e n2, que armazenam 2 notas em curso qualquer. A nota final do curso é calculada através da média ponderada da fórmula: media_final = (n1.2+n2*3)/5. com os valores das duas notas calcule, usando o interpretador Python3, a nota final do aluno final e atribua o resultado a variável media_final. Ao final mostre seu valor.")
n1 = int(input())
n2 = int(input())
media_final = (n1*2+n2*3)/5
print(media_final)

print("9. No interpretador Python3 crie uma variável x com um valor inteiro e logo a seguir uma variável digito que contém o último dígito (dígito das unidades) da variável x. O valor de x é desconhecido Exemplo: Se x for 73623, digito será 3. Use operações matemáticas para determinar o último dígito de um número inteiro.")
x = str(input())
z = len(x)
# 73623
print(x[z-1])

print("10. Considere uma variável seg, que armazena um tempo t em segundos. Escreva uma sequencia de instruções no interpretador Python3 que crie 3 variáveis, h, m e s, que contenham, respectivamente o tempo passado convertido em horas (h), minutos (m) e segundos (s).")
seg = 360
m = seg // 60 #segundo para minuto
h = seg // 360 #segundo para hora
print(seg, m , h)

print("11. Considere uma variável x com um valor inteiro desconhecido de 4 dígitos (exemplos: 1234 ou 1029 ou 3893). Usando apenas a variável x e expressões matemáticas crie uma variável chamada x_invertido que contenha o conteúdo de x com os valores invertido Exemplos:")
x = str(input())
i = 3
print (x, "| ", end="")
while i >= 0:
    print(x[i], end="")
    i -= 1

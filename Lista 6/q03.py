#3. Seja a função recursiva definida a seguir.
def f_rec(x):
    if x==0:
        return 0
    s = x%10
    n = x//10
    return s+f_rec(n) 
n = int(input())
print(n%10)
print(n//10)
print(f_rec(n))
#(a) Identifique o que faz a função - Soma o resto com o quociente. A função vai fazer varias chamadas, ate x = 0
#(b) Determine se há valores em que a função nunca termina. - Testei vários, nao encontrei nenhum
#(c) Escreva o valor de retorno para cada um dos valores de entrada a seguir:
#• 8 - 8
#• 19 - 10
#• 123 - 3+2+1 =6
#• 8192 - 2+9+1+8=20
#• 1000001 - 1+0+0+0+0+1=2
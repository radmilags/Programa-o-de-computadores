def bim1(l, a, b, c):
    s = [a, b ,c]
    s.sort()
    return (l+((s[1]+s[2])/2))*2
def bim2(l, a, b, c, d, e):
    s = [a, b, c, d, e]
    s.sort()
    return (l+((s[1]+s[2]+s[3])/3))*3

l,a,b,c = map(int,input().split())
l1,a1,b1,c1,d,e = map(int,input().split())
if bim1(l, a, b,c)+bim2(l1,a1,b1,c1,d,e)/5 >= 60: print("APROVADO")
else: print("NAO APROVADO")
'''Exemplo de entrada 1 Exemplo de saída 1
90 20 60 80 APROVADO
50 20 40 60 80 100'''
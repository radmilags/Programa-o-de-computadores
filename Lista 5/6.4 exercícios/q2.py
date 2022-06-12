s = list(input().split())
aux = s[0]
s[0] = s[1]
s[1] = aux
print(s)
def area(a,b):
    return a*b

def maior(a, b ,c ,d):
    maior1=a
    ans = "A"
    if b>maior1: 
        ans="B" 
        maior1 = b
    if c>maior1: 
        ans="C"
        maior1 = c
    if d>maior1: 
        ans="D"
        maior1 = d
    return ans

l1, p1 = map(int,input().split())
l2, p2 = map(int,input().split())
l3, p3 = map(int,input().split())
l4, p4 = map(int,input().split())
print(maior(area(l1,p1), area(l2,p2), area(l3,p3), area(l4,p4)))
'''
10 20 C
20 30
30 25
20 15

14 18 A
14 12
12 15
12 20
'''
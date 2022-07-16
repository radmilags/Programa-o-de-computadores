def f(a,b):
    if (a>=b):
        return (a+b)//2
    else:
        return f(f(a+2,b-1),f(a+1,b-2))
print(f(1,5))

'''Determine o valor de retorno para a chamada f(1,5). Para facilitar, faça um
desenho de todas as chamadas com seus respectivos valores.

f(
    f(a+2,b-1),f(a+1,b-2)
)
    f(a+2,b-1) ==== 3
        a+2=3 b-1 = 4
        f(3,4) a=3 e b=4
        f(
            f(a+2,b-1) = 4,f(a+1,b-2)=3
        )
            f(a+2,b-1) a=3+2 b=4-1
                f(5,3) (5+3)//2 = 4
            f(a+1,b-2) a=3+1 b=4-2 f(4,2) (4+2)//2 = 3
        f(4,3) (4+3)//2 = 3
    
    f(a+1,b-2) a+1=2 b-2=3
        f(2,3) a+1=3 b-2=1 == (3+1)//2 === 2

f(3,2) (3+2)//2 == 2
'''
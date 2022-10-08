import math
def quadratic(a, b, c):
    if not isinstance(a,(int,float)) or a==0:
        raise TypeError('a is wrong')
    if not isinstance(a,(int,float)):
        raise TypeError('b is wrong')
    if not isinstance(c,(int,float)):
        raise TypeError('c is wrong')
    deta=b**2-a*a*c
    if deta<0:
        print('no root')
    else:
        x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)
        return x1,x2
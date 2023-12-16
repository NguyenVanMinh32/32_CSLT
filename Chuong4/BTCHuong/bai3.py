def nhap():
    print('Nhap 3 so nguyen:')
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def giaipt(a,b,c):
    import math
    delta=b**2-4*a*c
    if delta>0:
        x1=int((-b+math.sqrt(delta))/(2*a))
        x2=int((-b-math.sqrt(delta))/(2*a))
        return x1,x2
    elif delta==0:
        x1=x2=int(-b/2*a)
        return x1,x2
    return delta
def inkq(x1,x2,delta):
    if delta>0:
        print('Phuong trinh co hai nghiem:')
        print('x1=',x1,'x2=',x2,sep='',end='\n')
    if delta==0:
        print('Phuong tring co nghiem kep:')
        print('x1=x2=',x1)
    if x1 is None:
        print('Phuong trinh vo nghiem')

a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)

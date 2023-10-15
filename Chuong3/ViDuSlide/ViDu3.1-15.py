import math
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
d=(b**2)-(4*a*c)
if d>0:
    print("Phuong trinh co 2 nghiem phan biet",)
    print('x1=',(-b+math.sqrt(d))/(2*a))
    print('x2=',(-b-math.sqrt(d))/(2*a))
elif d==0:
    print('Phuong trinh co nghiem kep, x=',-b/2*a)
else: print('Phuong trinh vo nghiem !!!')
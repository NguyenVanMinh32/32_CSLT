a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
import math
if(a+b)>c:
    if(b+c)>a:
        if(a+c)>b:
            p=(a+b+c)/2
            S=p*(p_a)*(p_b)*(p_c)
            print('Dien tich='+str(round(math.sqrt(S),3)))
            
else:print('Khong hop le')
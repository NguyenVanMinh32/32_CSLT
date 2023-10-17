a=int(input())
b=int(input())
c=int(input())
if(a+b)>c:
    if(b+c)>a:
        if(a+c)>b:
            if a*a==b*b+c*c:
                print('Tam giac vuong')
            elif b*b==a*a+c*c:
                print('Tam giac vuong')
            elif c*c==a*a+b*b:
                print('Tam giac vuong')
            elif a==b==c:
                print('Tam giac deu')           
            
else:print('Khong hop le')
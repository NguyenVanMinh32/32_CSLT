a=int(input())
b=int(input())
c=int(input())
if a>0 and b>0 and c>0 and (a+b)>c and (b+c)>a and (a+c)>b: 
    if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
        print('Tam giac vuong')
    elif a==b==c:
           print('Tam giac deu')
    else:print('Tam giac loai khac')                
else:print('Khong hop le')
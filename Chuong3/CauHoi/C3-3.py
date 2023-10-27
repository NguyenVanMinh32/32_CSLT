a=1
b=1
while b<=9 and a<=9:
    s=b*a
    print(s,end=' ')
    b=b+1
    if s%9==0:
        a=a+1
    else: b=b+1
    
        

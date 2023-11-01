
a=1
b=1
while a<=9:
    print(str(a*b).rjust(4),end=' ') 
    a=a+1
    while a%10==0 and b<9:
        a=1
        b=b+1
        print(' ')        
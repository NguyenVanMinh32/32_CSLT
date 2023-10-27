'''for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=' ')
    
    print()'''
a=1
b=1
while a<=9:
    print(str(a*b).rjust(4),end=' ') 
    a=a+1
    while a%10==0 and b<9:
        a=1
        b=b+1
        print(' ')        
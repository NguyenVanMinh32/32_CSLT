n=int(input('n='))
S=1
a=1
if 0<=n<=100:
    while a<=n:
        S=S*a
        a=a+1
    print(n,'!=',S,sep='')
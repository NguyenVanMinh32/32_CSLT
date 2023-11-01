n=int(input('n='))
i=1
while i<=n:
    if i%10 ==0:
        print(str(i).rjust(2),end='\n')
        i=i+1
    else :
        print(str(i).rjust(2),end=' ')
        i=i+1

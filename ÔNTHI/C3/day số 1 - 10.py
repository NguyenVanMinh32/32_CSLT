n=int(input('n='))
for i in range(1,n+1):
    print(str(i).rjust(2),end=' ')
    if i%10==0:
        print()
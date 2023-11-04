n=int(input('n='))
x=0
while n>=0:
    n=int(n/10)
    x=x+1
    if n==0:
        break
    
print(x)
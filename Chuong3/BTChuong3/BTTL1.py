n=int(input('n='))
S=1
a=1
#if 0<=n<=100:
for a in range (1,n+1,1):
    S=S*a
    a=a+1
print(n,'!=',S,sep='')
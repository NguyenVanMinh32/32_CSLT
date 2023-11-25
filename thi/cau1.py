a=int(input(''))
b=int(input(''))
n=0
if a<=b:
    for i in range(a+1,b+1,1):
        n+=i
    print(n)
else:print('')
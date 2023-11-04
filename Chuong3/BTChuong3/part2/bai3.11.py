a=0
b=0
while True:
    n=int(input('n='))
    if n>0:
        a=a+1
    elif n<0:
        b=b+1
    elif n==0:
        break
print(str(a)+' so duong')
print(str(b)+' so am')

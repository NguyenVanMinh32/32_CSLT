a=9
b=9
for i in range(1,a+1):
    for j in range(1,b+1):
        c=i*j
        print(str(c).rjust(2),end=' ')
    print()
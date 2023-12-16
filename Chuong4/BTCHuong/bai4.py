def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input('a='))
    b=int(input('b='))
    c=int(input('c='))
    return a,b,c
def max3(a,b,c):
    m=max(a,b,c)
    return m
def inkq(a,b,c,m):
    print('So lon nhat la:',m)
a,b,c=nhap()
m=max3(a,b,c)
inkq(a,b,c,m)
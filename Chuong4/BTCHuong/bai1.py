def nhap():
    n=int(input('n='))
    return n
def giaithua(n):
    if n==0:
        return 1
    else:
        return n*(giaithua(n-1))
def inkq():
    print(f'{n}!={x}')
n=nhap()
x=giaithua(n)
inkq()
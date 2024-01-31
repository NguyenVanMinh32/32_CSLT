def so_nguyen_to():
    n=int(input(''))
    return n
def check(n):
    for i in range(2,n):
        if n%i==0:
            da='SNT'
            break
    if n==1 or n==2:
        da="SNT"
    return da,n
def inkq(da,n):
    print(f'{n} là {da}')

n=so_nguyen_to()
da,n=check(n)
inkq(da,n)
def nhap():
    n=int(input('n='))
    return n
def inkq():
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=' ')

while True:
    n=nhap()
    inkq()
    print()
    tt=input('Tiep tuc khong?')
    if tt.lower()=='k':
        break
        
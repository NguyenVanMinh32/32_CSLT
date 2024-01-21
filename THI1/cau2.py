while True:
    n=int(input())
    if n<=0:
        print('Khong hop le, nhap lai!')
    if n>0:
        break
tong=0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        tong+=i
print(tong)

n=int(input('n='))
LaSoNT=0 
for i in range(2,n):
    if n%i==0:
        print(n,'Khong la SNT')
        break
    print(n,'la SNT')
    break
if n==1 or n==2:
    print(n,'la SNT')
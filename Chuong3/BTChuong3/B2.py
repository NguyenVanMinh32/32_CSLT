n=int(input('n='))
if n%1==0 and n%n==0:
    if n==2 or n==3 or n==7:
        print(n,'la SNT')
        if not(n%2==0 or n%3==0 or n%5==0):
            print(n,'la SNT')
        else:print(n,'khong la SNT')
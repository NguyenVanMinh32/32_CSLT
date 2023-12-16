n=int(input('Enter an integer (2 or greater):'))
a=2
if n<=2:
    print('Error, Please re-enter.')
else:
    print('The prime factors of',n,'are:')
    while n>1:
        if n%a==0:
            print(a,end='\n')
            n=n/a
        else:a=a+1

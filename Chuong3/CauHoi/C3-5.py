'''a=1
while a<=18:
    d=9
    while d>=0:
        print(end='')
        d=d-1
        b=1
        while b<=a:
            b=b+1
            print('%'.center(1),end='') 
            c=1
            while c<=b:
                c=c+2
                print(end='')
    a=a+2
    print(''.center(0))'''
a=16
while a>=0:
    b=0
    while a>=b:
        print(' ',end='') 
        b=b+2
        c=16
    while c>=a:
        print('*',end='')
        c=c-1
    print('')
    a=a-2
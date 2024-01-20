# a=b=int(input('='))

# for i in range(0,a+1):
#     b-=1
#     for j in range(0,b+1):
#         print('$',end='')
#     print()

a=b=8
c=-2
for i in range(0,a+1):
    b-=1
    c+=2
    for j in range(0,b+1):
        print(' ',end='')
    for h in range(0,c+1):
        print('*',end='')
        
    print()

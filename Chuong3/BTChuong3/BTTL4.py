a=float(input('a='))
b=float(input('b='))
tt=input('Toan Tu:')
while True:
    if tt=='+':
        print(a+b)
    elif tt=='-':
        print(a-b)
    elif tt=='*':
        print(a*b)
    elif tt=='/' and b!=0:
        print(a/b)
    else:print('cc')
    tt=input('Toan Tu:')
    if tt=='t' or tt=='T':
        break
    else: break
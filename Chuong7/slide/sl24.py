
# while True:
#     a=input()
#     b=input()
#     if a.isnumeric()==True and b.isnumeric()==True:
#         print('a+b='+str(int(a)+int(b)))
#         break
    
def nhap():
    while True:
        a=input('Nhập a:')
        b=input('Nhập b:')
        if a.isnumeric()==True and b.isnumeric()==True:
            break
        else:print('Nhập lại')
    return a,b
def tinh(a,b):
    print('a+b=',int(a)+int(b),sep='')
    
a,b=nhap()
tinh(a,b)
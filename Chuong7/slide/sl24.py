
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

# %%
#slide26
def checkpass():
    while True:
        pw=input('Nhập pass:')
        if str(pw).isalnum()==True:
            print(pw)
            break
        else:
            print('Nhập lại')


pw=checkpass()

# %%
#slide27
str='\n \n \n \t'
print(str.isspace())


# %%
#slide28
str="Bytesiwkkbf Lin"
print(str.istitle())

# %%
#slide30
def nhap():
    pw=input('Nhập pass:')
    return pw
def checkpass(pw):
    if len(pw)<8:
        print('Không hợp lệ')
    elif len(pw)>8:
        for char in pw:
                if not (char.isalpha() and char.isdigit() and char.isupper() and char.islower()):
                    print('Không hợp lệ')
                    nhap()
        else:print('Hợp lệ')
pw=nhap()
checkpass(pw)
    
    
    

# %%




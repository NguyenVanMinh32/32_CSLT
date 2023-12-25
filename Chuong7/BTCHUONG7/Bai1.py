a=0
b=0
c=0
def nhapckt():
    ckt=input()
    return ckt
def kiemtra(a,b,c,ckt):
    for char in ckt:
        if char.isupper():
            a+=1
        elif char.islower():
            b+=1
        elif char.isnumeric():
            c+=1
    return a,b,c,ckt
def inkq(a,b,c,ckt):
    print(f'In hoa:{a}\nIn thuong:{b}\nChu so:{c}\nKhac:{len(ckt)-a-b-c}')
    return a,b,c,ckt
ckt=nhapckt()
a,b,c,ckt=kiemtra()
inkq(a,b,c,ckt)

# TEST:
# Input: Python Programming Class @2021!
# Output:
# In hoa: 3
# In thuong: 19
# Chu so: 4
# Khac: 5


'''day=input()
a=0
b=0
c=0
for char in day:
    if char.isupper():
        a+=1
    elif char.islower():
        b+=1
    elif char.isnumeric():
        c+=1
print(f'In hoa:{a}\nIn thuong:{b}\nChu so:{c}\nKhac:{len(day)-a-b-c}')'''
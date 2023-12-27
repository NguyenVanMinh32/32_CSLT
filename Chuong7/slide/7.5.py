skt=input()
a=0
b=0
for char in skt:
    if char.isalpha:
        a+=1
    elif char.isnumeric:
        b+=1
print(f'chu cai:{a}\nso:{b}')
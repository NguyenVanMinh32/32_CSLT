a=0
b=0
so=((input())).split(' ')
print(so)
for char in so:
    if int(char)<0:
        a+=1
for char in so:
    if int(char)>0:
        b+=int(char)
print([a,b])
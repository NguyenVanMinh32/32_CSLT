a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
max=a
min=b
if max<b:
    max=b
if max<c:
    max=c
if min>a:
    min=a
if min>c:
    min=c
print('So lon nhat:',max)
print('So be nhat:',min)
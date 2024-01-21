n=input().split(' ')
dai=len(n)
for i in range(dai):
    a=(min(int(n[0]),int(n[i])))
n.remove(a)
for j in range(len(n)):
    b=(min(int(n[0]),int(n[j])))
n.remove(b)
for k in range(len(n)):
    c=(min(int(n[0]),int(n[k])))
print(a+b+c)
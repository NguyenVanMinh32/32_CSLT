x=int(input())
y=int(input())
n=int(input())
L=[]
for i in range(n):
    L=L+[int(input())]
def replace(L,x,y):
    for i in range(len(L)):
        if L[i]==x:
            L[i]=y
    return L
st=replace(L,x,y)
print(st)
        
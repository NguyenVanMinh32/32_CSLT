x=int(input())
k=int(input())
n=int(input())
L=[]
for i in range(n):
    L=L+[int(input())]
def add(L,x,k):
    if k > len(L):
        L=L+[x]
    else:
        L=L[:k]+[x]+L[k:]
    return L
st=add(L,x,k)
print(st)
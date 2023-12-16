x=int(input())
n=int(input())
L=[]
for i in range(n):
    L=L+[int(input())]
def delete(i,x):
    i=0
    while i<len(L):
        if L[i]==x:
            L[i:]=L[i+1:]
        else: i=i+1
    return L
st=delete(i,x)
print(st)
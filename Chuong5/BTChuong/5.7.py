n=int(input('n='))
L=[]
for i in range(n):
    M=L.copy()
    x=int(input(''))
    if x not in L:
        L=L+[x]
for j in range(len(M)):
    print(M[j],end=' ')
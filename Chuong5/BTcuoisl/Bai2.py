x=int(input())
# k=int(input())
n=int(input())
L=[]
for i in range(n):
    L=L+[int(input())]
def search(L,x):
    if x in L:
        for j in range (len(L)):
            if L[j]==x:    
                print(j)
    else: 
        print('None')
        return None
    return L
search(L,x)

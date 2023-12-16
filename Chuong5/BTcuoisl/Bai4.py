
n=int(input())
L=[]
for i in range(n):
    L=L+[int(input())]
def count(L):
    count=0
    for i in L:
        count=count+1
        print(count)
    
count(L)
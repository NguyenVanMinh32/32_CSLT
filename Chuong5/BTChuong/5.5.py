def input():
    n=int(input('n='))
    A=[]
    for i in range(n):
        A.append(int(input()))
    return A
def output(A):
    n=len(A)
    S=0
    for i in range(0,n):
        if i%2!=0:
            S=S+A[i]
    print('Tong=',S,sep='')
    
A=input()
output(A)
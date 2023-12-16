
n=int(input())
def input():
    
    A=[]
    for i in range(n):
        A.append(int(input()))
    return A
def output(A):
    n=len(A)
    B=list(A)
    for i in range(0,n-1,2):
       B[i]=A[i+1]
       B[i+1]=A[i]
    for j in range(0,len(B),1):
        print(B[j],end=' ')
A=input
output(A)
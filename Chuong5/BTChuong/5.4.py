def input():
    n=int(input('n='))
    A=[]
    for i in range(n):
        A.append(int(input()))
    return A
def output(A):
    B=list(reversed(A))
    print(B)
    B.sort()
    print(B)
A,n=input()
output(A)
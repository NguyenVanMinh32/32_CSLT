def input():
    n=int(input('n='))
    L=[]
    for i in range(n):
        L=L+[int(input())]
    x=int(input('x='))
    return L,x
def firstandlast(L):
    if len(L)>=2:
        result=[L[0],L[-1]]
        print(result)
        return result
    else:
        print('error')
        return None
    return L
def search(L,x):
    if x in L:
        print('True')
        return True
    else:
        print('False')
        return False
L,x=input()
firstandlast(L)
search(L,x)
  
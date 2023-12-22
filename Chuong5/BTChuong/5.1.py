def iinput():
    L=[]
    n=int(input())
    for i in range(n):
        L=L+[int(input())]
    return L,n,x
def firstandlast(L):
    if len(L)>=2:
        result=[L[0],L[-1]]
        print(result)
        return result
    else:
        print('error')
        return None

def search(L,x):
    if x in L:
        print('True')
        return True
    else:
        print('False')
        return False
    
L,x=iinput()
firstandlast(L)
search(L,x)
'''def get_input():
    L = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        L.append(int(input("Enter element {}:".format(i + 1))))
    x = int(input('Enter the value of x: '))
    return L, x

def first_and_last(L):
    if len(L) >= 2:
        result = [L[0], L[-1]]
        print(result)
        return result
    else:
        print('Error: List should have at least 2 elements.')
        return None

def search(L, x):
    if x in L:
        print('True')
        return True
    else:
        print('False')
        return False

L, x = get_input()
first_and_last(L)
search(L, x)
'''
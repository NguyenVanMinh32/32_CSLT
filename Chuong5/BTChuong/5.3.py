def iinput():
    n=int(input('n='))
    L=[]
    for i in range(n):
        L=L+[int(input())]
    return L
def inkq(L):
    count=0
    S=0
    positive=0
    for j in L:
        if j>0:
            count=count+1
        if j%2==0:
            S=S+j
            positive+=1
        if positive==0:
            average=0
        elif positive!=0:
            average=S/positive
    print('SND=',count,sep='')
    print("TBC=", average,sep='')

L=iinput()
inkq(L)

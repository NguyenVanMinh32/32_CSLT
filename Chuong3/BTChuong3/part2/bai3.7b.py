while True:
    n=int(input(''))
    s=1
    if n<0:
        break
    for i in range(1,n+1):
        s=s*i
    print(s)
    
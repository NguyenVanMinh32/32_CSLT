while True:
    i=1
    s=1
    n=int(input(''))
    if n<0:
        break
    while i<=n:
        s=s*i
        i=i+1
    print(s)
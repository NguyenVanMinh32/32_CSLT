n=int(input(''))
soluong=0
while n>5:
    if n%3==0 and n%5==0:
        soluong+=1
        n-=1
    else:n-=1
print(soluong)
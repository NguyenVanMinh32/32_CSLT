n = int(input())
d = 1 
while d*10 <= n:
    d *= 10
while d > 0:
    x = n//d
    if x == 0:
        print('A', end = '')
    if x == 1:
        print('B', end = '')
    if x == 2:
        print('C', end = '')
    if x == 3:
        print('D', end = '')
    if x == 4:
        print('E', end = '')
    if x == 5:
        print('F', end = '')
    if x == 6:
        print('G', end = '')
    if x == 7:
        print('H', end = '')
    if x == 8:
        print('K', end = '')
    if x == 9:
        print('L', end = '')
    n %= d 
    d //= 10
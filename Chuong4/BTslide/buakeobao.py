import random
def oan_tu_ti():
    n = int(input("Humman: "))
    if n==0:
        000
    elif 0 < n <= 3:
        m = random.randint(1, 3)
        if n == m:
            tinh_trang = "Draw"
        elif (n == 1 and m == 3) or (n == 2 and m == 1) or (n == 3 and m == 2):
            tinh_trang = "Human win"
        else:
            tinh_trang = "Computer win"
        print("Computer:", m)
        print("Result:", tinh_trang)
        print()
    else: print('Nhap lai')
    if n!=0: 
        oan_tu_ti()
    
oan_tu_ti()
total=0.0
count=0
price=input("Nhap gia(Nhap rong de thoat):")
while price !="":
    price=float(price)
    total+=price
    count+=1
    price=input("Nhap gia(Nhap rong de thoat):")
print ("Tong chi phi:",total)
pennies=total*100
remainder=pennies%5
if remainder <2.5:
    cash_payment=pennies_remainder
else:
    cash_payment=pennies+(5_remainder)
cash_payment /=100
print("So tien phai tra bang tien mat($):",cash_payment)
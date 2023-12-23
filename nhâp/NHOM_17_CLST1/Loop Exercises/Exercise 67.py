age=input("Nhap tuoi(Enter de ket thuc):")
S=0
while age !="":
    age=int(age)
    if age<=2:
        cost=0
    elif 3<=age <=12:
        cost=14
    elif age>=65:
        cost=18
    else:
        cost=23
    S+=cost
    age =input()
print("Tong chi phi :",round(S,2))

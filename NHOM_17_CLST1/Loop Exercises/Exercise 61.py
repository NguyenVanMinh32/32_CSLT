i=0
j=0
num=float(input("Nhap mot so (0 de ket thuc):"))
if num==0:
    print("Loi:Ban phai nhap it nhat mot so khac 0")
else:
    while num !=0:
        i+=num
        j+=1
        num=float(input("Nhap mot so (0 de ket thuc):"))
    tbc=i/j
    print("Trung binh cong cac so:",tbc)
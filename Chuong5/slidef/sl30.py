students=["An","Binh","Lan","Thanh","Minh"]
#Cách 1
for x in students:
    print(x ,end=", ")
#Cách 2: sử dụng cấu trúc for
for x in range(len(students)):
    print(students[x] ,end=", ")
#Cách 2: sử dụng cấu trúc while
x=0
while x<len(students):
    print(students[x],end=", ")
    x=x+1
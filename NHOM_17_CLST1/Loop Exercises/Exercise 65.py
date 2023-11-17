import math
p=0
x1=None
x2=None
y1=None
y2=None
x1=float(input("Enter the x part of the coordinate:"))
y1=float(input("Enter the y part of the coordinate:"))
x_dau=x1
y_dau=y1
while True:
    x2=input("Enter the x part of the coordinate: (blank to quit):")
    if x2=="":
        break
    x2=float(x2)
    y2=float(input("Enter the y part of the coordinate:"))
    distance = math.sqrt((x2- x1)**2 + (y2 - y1)**2)
    p+=distance
    x1=x2
    y1=y2
distance=((x_dau-x1)**2+(y_dau-y1)**2)**0.5
p+=distance
print("The perimeter of that polygon is",p)

   

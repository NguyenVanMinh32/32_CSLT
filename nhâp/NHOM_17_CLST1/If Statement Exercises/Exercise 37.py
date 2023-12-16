a=int(input("Number of sides:"))
if a==3:
    print("A shape with",a,"sides is called a triangle")
elif a==4:
    print("A shape with",a,"sides is called a quadrilateral")
elif a==5:
    print("A shape with",a,"sides is called a pentagon")
elif a==6:
    print("A shape with",a,"sides is called a hexagon")
elif a==7:
    print("A shape with",a,"sides is called a heptagon")
elif a==8:
    print("A shape with",a,"sides is called a octagon")
elif a==9:
    print("A shape with",a,"sides is called a nonagon")
elif a==10:
    print("A shape with",a,"sides is called a decagon")
else:
    print("Error: The number of sides must be between 3 and 10.")
side1 = float(input('Enter the length of the first side: '))
side2 = float(input('Enter the length of the second side: '))
side3 = float(input('Enter the length of the third side: '))
if side1 == side2 == side3:
    print('This is an equilateral triangle.')
elif side1 == side2 or side1 == side3 or side2 == side3:
    print('This is an isosceles triangle.')
elif side1 == side2+side3 or side3 == side1+side2 or side2 == side3+side1:
    print('This is not a triangle')
elif (side1**2==side2**2+side3**2) or (side2**2== side3**2+side1**2) or (side3**2 == side2**2+side1**2):
    print('This is a right triangle')
else:
    print('This is a scalene triangle.')
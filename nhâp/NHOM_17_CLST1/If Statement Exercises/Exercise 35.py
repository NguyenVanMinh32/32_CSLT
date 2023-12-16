human= int(input("The age of the dog in human years: "))
if human < 0:
    print("Error")
elif human<= 2:
    dog= int(human * 10.5)
else:
    dog= int(21 + (human _ 2) * 4)
print("A ",human,"_year_old dog is equivalent to a ",dog,"_year_old human in terms of age.",sep="")
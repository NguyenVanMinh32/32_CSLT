month=input("Enter the month:")
day=int(input("Enter the day:"))
if (month=="January") or (month=="january") and (day==1):
    print("New year’s day")
elif (month=="July") or (month=="july") and (day==1):
    print("Canada day")
elif (month=="December") or (month=="december") and (day==25):
    print("Christmas day")
else:
    print("The entered month and day do not correspond to a fixed-date holiday")
S=0
i=0
while True:
    grade=input("Enter a letter grade(or blank to quit):")
    if grade =="":
        break
    if grade =="A+":
        diem=4.0
    elif grade=="A":
        diem=4.0
    elif grade=="A_":
        diem=3.7
    elif grade=="B+":
        diem=3.3
    elif grade=="B":
        diem=3.0
    elif grade=="B_":
        diem=2.7
    elif grade=="C+":
        diem=2.3
    elif grade=="C":
        diem=2.0
    elif grade=="C_":
        diem=1.7
    elif grade =="D+":
        diem=1.3
    elif grade=="D":
        diem=1.0
    elif grade=="D_":
        diem=0.7
    elif grade=="F":
        diem=0.0
    else:
        print("Invalid letter grade.Try again.")
        continue
    S+=diem
    i+=1
if i>0:
    gpa=S/i
    print("Grade point average:",round(gpa,1))
else:
    print("No grades entered.")
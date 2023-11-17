def C-to-F(C):
    return C*9/5+32
print("Do C | Do F")
for C in range(0,101,10):
    F=C-to-F(C)
    print(str(C).rjust(4),"|",F)

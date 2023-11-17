# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j, end="\t")
#     print()
a=1
b=10
print("      ", end="")
for i in range(a, b+1):
    print("%3d" %i,'  ',end="")
print()
print()
for i in range(a, b+1):
    print("%3d" %i,'  ', end="")
    for j in range(a, b+1):
        print("%3d" %(i*j),'  ', end="")
    print()

st1 = input("st1: ")
st2 = input("st2: ")
count = 0
a=len(st2)
for i in range(len(st1)):
    if st1[i:i+a].lower() == st2.lower():
        count += 1
print(count)
print(st1.find(st2))
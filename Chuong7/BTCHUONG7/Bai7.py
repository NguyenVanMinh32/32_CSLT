ckt=input()
a=ckt.find('@')
b=ckt.find('.com',a)
i=0
while True:
    i=i+1
    c=ckt.find(' ',a-i)
    if c>=0:
        break
print(ckt[(c+1):(b+4)])

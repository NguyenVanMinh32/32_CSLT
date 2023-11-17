import random
number=0
greatest-num=random.randint(1,100)
pre-number=0
update-time=0
print(greatest-num)
for i in range(99):
    number=random.randint(1,100)
    if greatest-num<number:
       greatest-num=number
       print(number,'<== Update')
       update-time+=1
    else:print(number)   
print(f'The maximum value found was {greatest-num}',f'The maximum value was updated {update-time} times',sep='\n')

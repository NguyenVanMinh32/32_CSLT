import random
number=0
greatest_num=random.randint(1,100)
pre_number=0
update_time=0
print(greatest_num)
for i in range(99):
    number=random.randint(1,100)
    if greatest_num<number:
       greatest_num=number
       print(number,'<== Update')
       update_time+=1
    else:print(number)   
print(f'The maximum value found was {greatest_num}',f'The maximum value was updated {update_time} times',sep='\n')

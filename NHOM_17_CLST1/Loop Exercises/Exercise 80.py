import random
total-flips=0
for i in range(10): 
    flips=0 
    consecutive-count-H=0
    consecutive-count-T=0
    while True:
        result=random.choice(['H','T'])
        flips+=1
        if result=='H' and consecutive-count-H<3 and consecutive-count-T<3: 
            consecutive-count-H+=1
            consecutive-count-T=0
        elif result=='T'and consecutive-count-H<3 and consecutive-count-T<3:
            consecutive-count-T+=1
            consecutive-count-H=0
        print(result,end=' ')
        if consecutive-count-H==3 or consecutive-count-T==3:
            break
    total-flips+=flips
    print(f'({flips} flips)')
print(f'On average, {total-flips/10} flips were needed.')



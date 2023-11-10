#pp chia đôi
decimal=int(input('Decimanl:'))
b=''
while decimal>0:
    a=decimal%2
    decimal=(decimal//2)
    b=str(a)+b
print('The equivalent binary number is',f'{b}')
   

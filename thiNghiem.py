#print(int(2453.35,10))
'''print('Nhập tên của bạn:')
x = input()
print('QuanTriMang xin chào bạn, ' + x)'''
#print('Hello\nWorld\n!')
#len('fdutyu')
'''a = bytes('ŽString', encoding = 'utf-8')
s = str(a, encoding = 'ascii', errors ='replace')
print(s)'''
#print(float(25))
'''import math
r=float(input('Nhap vao ban kinh cua duong tron:'))
dt=math.pi*r**2
cv=2*r*math.pi
print('Dien tich cua duong tron co ban kinh',r,'la',round(dt,1))
print('Chu vi cua duong tron co ban kinh',r,'la',round(cv,1))'''
'''a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
print(max(a,b,c))'''
'''n=int(input('n='))
S=1
if n>0:
    while True:
        S=S*n
        n=n-1
        if n==0:
            break
else: 
    while True:
        S=S*n
        n=n+1
        if n==0:
            break
print(S)'''
# max_length = 3  # Đặt giới hạn số ký tự
# user_input = input('Nhập chuỗi: ')[:max_length]
# print('Chuỗi đã nhập:', user_input)
'''noise_levels = {
    'Jackhammer': 130,
    'Gas lawnmower': 106,
    'Alarm clock': 70,
    'Quiet room': 40}
user_input = float(input('Enter a sound level in decibels: '))

# Initialize variables to keep track of the closest noises
lower_noise = None
higher_noise = None

# Check the user's input against the noise levels
for noise, level in noise_levels.items():
    if user_input == level:
        print(f'The noise is: {noise}')
        break
    elif user_input < level:
        higher_noise = noise
    else:
        lower_noise = noise

# Provide appropriate messages based on the user's input
if lower_noise and higher_noise:
    print(f'The noise is between {lower_noise} and {higher_noise}.')
elif lower_noise:
    print(f'The noise is quieter than {lower_noise}.')
elif higher_noise:
    print(f'The noise is louder than {higher_noise}.')'''
    ##
# Compute the greatest common divisor of two 
# positive integers using a while loop.
#

# Read two positive integers from the user
n =  363
m =  488

d =  min (n, m)

print(d)



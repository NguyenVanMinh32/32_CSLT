'''noise_levels = {
    "Jackhammer": 130,
    "Gas lawnmower": 106,
    "Alarm clock": 70,
    "Quiet room": 40}
user_input = float(input("Enter a sound level in decibels: "))

# Initialize variables to keep track of the closest noises
lower_noise = None
higher_noise = None

# Check the user's input against the noise levels
for noise, level in noise_levels.items():
    if user_input == level:
        print(f"The noise is: {noise}")
        break
    elif user_input < level:
        higher_noise = noise
    else:
        lower_noise = noise

# Provide appropriate messages based on the user's input
if lower_noise and higher_noise:
    print(f"The noise is between {lower_noise} and {higher_noise}.")
elif lower_noise:
    print(f"The noise is quieter than {lower_noise}.")
elif higher_noise:
    print(f"The noise is louder than {higher_noise}.")'''
nl=int(input('noise level:'))
Jackhammer =130    
GasLawnmower= 106   
AlarmClock =70
QuietRoom = 40
if nl>130:
    print('The noise is louder than Jackhammer')
elif 106<nl<130:
    print('The noise is between Gas Lawnmower and Jackhammer')
elif 70<nl<40:
    print('The noise is between Alarm Clock and Gas Lawnmower')
elif 0<nl<40:
    print('The noise is quieter than Quiet Room')
elif nl==130:
    print('The noise is Jackhammer')
elif nl==106:
    print('The noise is Gas Lawnmower')
elif nl==70:
    print('The noise is Alarm Clock')
elif nl==40:
    print('The noise is Quiet Room')
else:print('You entered the wrong noise level')

    
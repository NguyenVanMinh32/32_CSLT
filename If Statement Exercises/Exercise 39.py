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

    
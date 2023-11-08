HzNote={"C": 261.63,
        "D": 293.66,
        "E": 329.63,
        "F": 349.23,
        "G": 392.00,
        "A": 440.00,
        "B": 493.88}
note=input('Note (Ex: C4, D4, B3, ...):')[:2]
notename=note[0]
oktav=int(note[1])
if notename in HzNote and 0<=oktav<=8:
    Hz=HzNote[notename]/(2**(4-oktav))
    print('The frequency of',note,'is',Hz)
else:print('Invalid note')

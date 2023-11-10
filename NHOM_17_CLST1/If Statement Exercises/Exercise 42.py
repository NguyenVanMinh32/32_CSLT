freq=float(input("Enter the frequency:"))
if (260.63<=freq<=262.63):
    note="C4"
elif (292.66<=freq<=294.66):
    note="D4"
elif (328.63<=freq<=330.63):
    note="E4"
elif (348.23<=freq<=350.23):
    note="F4"
elif (391.00<=freq<=393.00):
    note="G4"
elif (439.00<=freq<=441.00):
    note="A4"
elif (492.88<=freq<=494.88):
    note="B4"
else:
    note="There is no need to consider notes from other octaves."
print(note)
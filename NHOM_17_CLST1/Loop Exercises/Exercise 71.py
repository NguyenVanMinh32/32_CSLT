x = float(input("x="))
guess = x / 2
epsilon = 10 ** -12
while guess ** 2 - x > epsilon or x - guess ** 2 > epsilon:
    guess = (guess + x / guess) / 2
print("The square root of", x, "is approximately", guess, ".")

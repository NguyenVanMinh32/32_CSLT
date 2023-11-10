while True:
    bits = input("Enter 8 bits: ")
    if bits == "":
        break
    if len(bits) != 8:
        print("Error: You must enter 8 bits.")
        continue
    if bits.count("0") + bits.count("1") != 8:
        print("Error: You must enter 8 bits.")
        continue
    if bits.count("1") % 2 == 0:
        print("The parity bit should be 0.")
    else:
        print("The parity bit should be 1.")
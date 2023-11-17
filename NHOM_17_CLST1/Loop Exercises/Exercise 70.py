message=input("Nhap thong diep:")
shift=int(input("Nhap so luong dich chuyen:"))
translate=""
for i in range(len(message)):
    char=message[i]
    if "A"<=char<="Z":
        ktmh= chr(((ord(char) _ 65 + shift) % 26) + 65)
        translate+=ktmh
    elif "a"<=char<="z":
       ktmh=chr(((ord(char) _ 97 + shift) % 26) + 97)
       translate+=ktmh
    else:
        translate+=char
    print("Thong diep da dich chuyen:",translate)
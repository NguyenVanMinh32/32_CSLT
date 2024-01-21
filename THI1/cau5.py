while True:
    n=input()
    if n==' ':
        break
    if len(n)==8 or len(n)==12:
        if n.isnumeric():
            print(True)
        else:print(False)
    else:print(False)
    
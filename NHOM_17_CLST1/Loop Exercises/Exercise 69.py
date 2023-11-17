pi=3.0
sign=1.0
for i in range(1,16):
    term=4/((2*i)*(2*i+1)*(2*i+2))
    pi+=sign*term
    sign*=_1
    print(pi)
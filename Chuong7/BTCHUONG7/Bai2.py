skt=input()
skt=skt.strip().capitalize().split()
skt=(' '.join(skt))
for char in [',',':',';','.']:
    skt=skt.replace(' '+char,char)
print(skt)

'''TEST:
Input: Xin Chào , tôi là sInh viêN
Output: Xin chào, tôi là sinh viên'''
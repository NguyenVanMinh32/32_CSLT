#cách 1
'''pw=input()
ktdb=['@','#','$']
if 6<=len(pw)<=17:
    if any(char.islower() for char in pw) and any(char.isupper() for char in pw) and any(char.isdigit() for char in pw) and any(char in ktdb for char in pw):
        print("True")
    else:print('False')
else:print('False')'''
#cách 2
'''pw=input()
import re
if 6<=len(pw)<=17:
    if re.search('[a-z]',pw) and re.search('[0-9]',pw) and re.search('[A-Z]',pw) and re.search('[@#$]',pw):
        print('True')
    else:print('False')
else:print('False')'''

#def 
def nhap():
    pw=input()
    return pw
def ktra(pw):
    a=0
    import re
    if 6<=len(pw)<=17:
        if re.search('[a-z]',pw) and re.search('[0-9]',pw) and re.search('[A-Z]',pw) and re.search('[@#$]',pw) :
            a=a+1
            return True
        else: return False
    else: return False
def inkq(a):
    if a==1:
        print('True')
    else:
        print('False')
    
pw=nhap()
a=ktra(pw)
inkq(a)
#noie eNFt59
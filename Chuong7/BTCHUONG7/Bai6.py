nhi_phan=(input()).split(',')
dsnp=[]
for char in nhi_phan:
    if (int(char,2))%3==0:
        dsnp.append(char)
    else: pass
if len(dsnp)>0:
    print(','.join(dsnp))
else:
    print()
    

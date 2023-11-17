a=int(input('Tieu thu='))
if a<101:
    tiendien=550*a
if 100<a<151:
    tiendien=55000+750*(a_100)
if 150<a<201:
    tiendien=92500+950*(a_150)
if a>200:
    tiendien=140000+1350*(a_200)
print('Phai tra='+str(round(tiendien*1.1,1)))
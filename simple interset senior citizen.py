p=int(input("enter p "))
n=int(input("enter n "))
sc=input("senior citizex(y/n)")
d=input("m/f")
if sc=="y" and d=="m":
    print((p*n*15)/100)
elif sc=="y" and d=="f":
    print((p*n*12)/100)
else:
    print((p*n*10)/100)
        

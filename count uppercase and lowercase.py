n="rainBOW"
x="abcdefijklmnopqrstuvwxyz"
u=0
l=0
for i in n:
    if i in x:
        u+=1
    else:
        l+=1
print("lowercase=",u)
print("uppercase=",l)

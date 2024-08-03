n=0
m=0
u=0
l=0
while(n!="*"):
    n=input("enter n ")
    if n.isupper():
        u+=1
    elif n.islower():
        l+=1
    elif n.isdigit():
        m+=1
print("upper",u)
print("lower",l)
print("numbers",m)

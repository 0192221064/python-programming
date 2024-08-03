n=int(input("enter n "))
m=str(n)
c=input("enter choice(A/D/B):")
for i in c:
    if i=="A":
       a=sorted(m)
    elif i=="D":
        b=a[::-1]
    elif i=="B":
       a=sorted(m)
       b=a[::-1]
s="".join(a)
f="".join(b)
print("asennding",s)
print("desending",f)

    

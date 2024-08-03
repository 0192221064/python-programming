n=3025
m=str(n)
a=m[:len(m)//2]
b=m[len(m)//2:]
c=int(a)+int(b)
d=c**2
if(n==d):
    print("tec number")
else:
    print("not tec number")

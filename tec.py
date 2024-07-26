n=3025
a=str(n)
s=a[:len(a)//2]
r=a[len(a)//2:]
a=int(s)+int(r)
result=a**2
if(result==n):
    print("tec number")
else:
    print("not a tec number")

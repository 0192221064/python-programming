n=int(input("enter n"))
m=int(input("enter m"))
v=[]
c=[]
if n>m:
    t=n
    n=m
    m=t
for i in range(n+1,m):
    if i%2==0:
        v.append(i)
    elif i%2!=0:
        c.append(i)
print("odd numbers",c)
print("even numbers",v)

n=int(input("enter n"))
m=int(input("enter m"))
v=[]
if n>m:
    t=m
    m=n
    n=t
for i in range(n+1,m):
    if i>0:
        for j in range(2,i):
            if i%j==0:
                if i in v:
                    break
                else:
                    v.append(i)
                
print(v)
               

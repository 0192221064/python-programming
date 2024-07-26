n=int(input("enter n"))
m=int(input("enter m"))
f=0
for i in range(n+1,m):
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
        else:
            f=0
    if(f==0):
        print(i)

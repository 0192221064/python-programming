a=int(input("enter a"))
b=int(input("enter b"))
s=[]
for i in range(a,b):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
            else:
                if i in s:
                   break
                else:
                   s.append(i)
print(s)

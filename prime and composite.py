n=[1,2,3,4,5,6,7,8]
p=[]
c=[]
for i in n:
    if i>0:
        for j in range(2,i):
            if i%j==0:
                if i not in p:
                    p.append(i)
                elif i not in c:
                    c.append(i)
print(p)
print(c)

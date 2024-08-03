n=[1,2,3,1,1,3]
c=0
for i in range(len(n)):
    for j in range(len(n)):
       if n[i]==n[j] and i<j:
           c+=1
print(c)

n=100
v=[]
c=0
for i in range(1,n+1):
     if n%i==0:
         v.append(i)
         c+=1
print("no of factors",c)
print("first four factors",v[0:4])
         
    

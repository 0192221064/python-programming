n=5
fac=1
sum=0
for i  in range(1,n+1):
    fac=fac*i
    sum=sum+fac/i
print(int(sum))

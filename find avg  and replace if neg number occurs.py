a=[9,0,4,-1,5,6]
s=sorted(a)
print(s)
n=len(a)
av=int(sum(a)/n)
for i in range(len(a)):
    if a[i]<0:
       a[i]=av
print(a)

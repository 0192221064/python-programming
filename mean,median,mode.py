a=[1,2,3,4,1,1]
n=len(a)
s=sum(a)
mean=s/n
print("mean:",mean) 
a.sort() 

if (n%2==0):
	median1 = a[n//2] 
	median2 = a[n//2 - 1] 
	median = (median1 + median2)/2
else: 
	median = a[n//2] 
print("median",median)
 

mode = max(a, key=a.count)
print("mode",mode)

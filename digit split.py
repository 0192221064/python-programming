n=int(input("enter n"))
d=[int(digit) for digit in str(n)]
sum=0
for i in d:
    sum=sum+i
x=sum**2
if(x==n):
    print("tec number")
else:
    print("not tec number")

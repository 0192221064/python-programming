n=int(input("enter n"))
sum=0
d=[int(digit) for digit in str(n)]
for i in d:
    sum=sum+i**3
if(sum==n):
    print("amstrong number")
else:
    print("not amstrong number")

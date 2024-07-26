n=int(input(" enter n value" ))
a=0
b=1
for n in range(1,n):
    c=a+b
    a=b
    b=c
print(c)

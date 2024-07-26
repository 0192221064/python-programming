n= [int(input("Enter the numbers ")) for _ in range(8)]
p=0
c=0
for i in n:
    if i>1:
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            p+=1
        else:
            c+=1
print("prime count",p)
print("composite count",c)

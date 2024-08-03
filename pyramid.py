n = 4
a=1
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
        
    for k in range(i):
        print(a,"", end="")
        a+=1
    print()

def rec_fac(n):
    if n==1 or n==0:
        return 1
    else:
        return n*rec_fac(n-1)
n=int(input("enter n"))
print(rec_fac(n))

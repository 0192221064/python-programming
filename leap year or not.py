date = input("Enter the date to be checked: ")
c=date.split("/")
b = list(map(int,c))
i=(b[2])
if i%4==0:
    print("leap")
else:
    print("not leap")
x=i%4
if x!=0:
    print("04/11/",i-1)
else:
    print("04/11/",i+1)

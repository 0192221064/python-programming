a=input("enter strin")
x="aeiouAEIOU"
s=0
v=0
c=0
for i in a:
    if i in x:
        v+=1
    elif i.isspace():
        s+=1
    else:
        c+=1
print(v,c)
maximum_value=max(v,c)
print("maximum value is:",maximum_value)

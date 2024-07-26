n="saveetha school of engineering"
x="aeiouAEIOU"
v=0
c=0
s=0
for i in n:
    if i in x:
        v+=1
    elif(i.isspace()):
        s+=1    
    else:
        c+=1
print(v)
print(c)

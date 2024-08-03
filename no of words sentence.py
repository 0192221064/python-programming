w=0
s=0
strr=input()
l=len(strr)
for i in strr:
    if i==" ":
        w+=1
    elif i== ".":
        s+=1
        w+=1
print(l,w,s)

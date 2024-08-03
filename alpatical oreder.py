n=input("enter n: ")
v=[]
c=[]
x="aeiouAEIOU"
for i in n:
    if i in x:
        v.append(i)
    elif i not in x:
        c.append(i)
s=sorted(v)
m=",".join(s)
r=sorted(c)
q=",".join(r)
print("vowels: ",m)
print("consonants: ",q)

s="TEMPLE"
v=[]
c=0
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            if s[i]==s[j]:
                if s[i] in v:
                    break
                else:
                    v.append(s[i])
                    c+=1
print(v,c)
                    
                
                

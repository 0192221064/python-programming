a=[2,2,4,4,5,6,7,8,12,12]
v=[]
for i in range(len(a)):
    for j in range(len(a)):
        if(i!=j):
            if(a[i]==a[j]):
                if a[i] in v:
                    break
                else:
                    v.append(a[i])
print(v)

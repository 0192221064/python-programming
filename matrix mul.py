n=input(" enter strin" )
x="aeiouAEIOU"
vow_count=0
cons_count=0
for i in n:
    if i in x:
        vow_count+=1
        
    else:
        cons_count+=1
       
print(vow_count,cons_count)

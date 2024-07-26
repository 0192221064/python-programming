n=input("enter n")
vow=0
cons=0
x="aeiouAEIOU"
for i in n:
    if i in x:
        vow+=1
    else:
        cons+=1
print("vowels",vow)
print("consonants",cons)

str1=input("enter str1:" )
str2=input(" enter str2:" )
for i in str1:
    if i in str2:
        x=1
    else:
        x=0
if(x==1):
   print("anagram")
else:
   print(" not anagram")

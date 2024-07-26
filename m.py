s=" I am a programmer "
tar="p"
index="not found"
if tar in s:
    print("yes")
    
else:
    print("no")
for i in range(len(s)):
    if s[i]==tar:
      index=i
print(index)

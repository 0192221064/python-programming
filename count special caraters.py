s = "Modi Birthday @ September 17, #&$% is the wishes code for him."
c = 0
sp= "!@#$%^&*()-_=+[]{}|;:'\"<>?/\\`~"
for char in s:
       if char in sp:
         c += 1

print("Number of special characters:", c)

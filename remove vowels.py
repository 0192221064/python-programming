t="we can play the game"
v="aeiouAEIOU"
n = ""
for i in range(len(t)):
    if t[i] not in v:
        n = n + t[i]
t = n
print(t)


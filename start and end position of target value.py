n = [5, 7, 7, 8, 8, 10]
t=8
for i in range(len(n)):
    if n[i]==t:
        start=i-1
        end=i
print(start,end)

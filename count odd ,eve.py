n=[1,2,3,4,5,6,7,8,9]
eve=0
odd=0
for i in range(len(n)):
    if(n[i]%2==0):
        eve+=1
    elif(n[i]%2!=0):
        odd+=1
print("count of even numbers:",eve)
print("count of odd numbers:",odd)

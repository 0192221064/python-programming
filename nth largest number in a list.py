def lar(v,n):
        if v==4:
           return print(n[v-1])
        elif v==0:
            return print("invalid entry")
        elif  v==1:
           return  print(n[v])
        elif v==-5:
            return print("no numbers")
        elif v=="%":
            return print("invalid symbol")
n=[14, 67, 48, 23, 5, 62]
t=(4,0,-5,1,"%")
for v in n:
    print(lar(v,n))

m=[[2,3,4],[1,5,6],[1,2,3]]
r_sum=0
c_sum=0
d_sum=0
for i in range(len(m)):
        for j in range(len(m)):
            r_sum+=m[i][j]
        print("sum of",i,"row is",r_sum)
        r_sum=0
for i in range(len(m)):
    for j in range(len(m)):
        c_sum+=m[j][i]
    print("sum of",i,"column is",c_sum)
    c_sum=0
for i in range(len(m)):
    for j in range(len(m)):
        if(i==j):
            d_sum+=m[i][j]
print("sum of dia",d_sum)

a=[[2,1],[3,4]]
b=[[3,1],[1,2]]
c=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            c[i][j]+=a[i][k]*b[k][j]
for i in c:
    print(i)

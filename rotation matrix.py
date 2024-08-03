m=[[1,2,3],
   [4,5,6],
   [7,8,9]]
for i in range(len(m)):
    for j in range(len(m)):
        m[i][j]=m[j][i]
for i in range(len(m)):
    m.reverse()
for i in m:
    print(i)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r=[]
c=[0] * len(matrix[0])
for r in matrix:
    row_sum = sum(r)
    row_sums.append(row_sum)
    for i, val in enumerate(r):
        c[i] += val


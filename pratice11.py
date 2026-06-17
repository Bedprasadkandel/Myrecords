sum=0
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in range(len(matrix)): #  index:x===0,1,2 but length==1,2,3
    sum=sum+matrix[i][i]
print(sum)
# #nested loop
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# value=matrix[1]
# print(value)
#####################################################################
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]]
# for x in matrix:
#     for value in x: 
#          print(x)
################################################################
# matrix=[ 1,2,3]
# result=sum(matrix)
# print(result)
##########################################Sum of number from 1-9 in matrix:

# sum=0
# matrix=[
#      [1,2,3],
#      [4,5,6],
#      [7,8,9]
# ]
# for row in matrix:
#      for num in row:
#       sum=sum+num
# print("Sum of matrix:",sum)
# # #Diagonal sum ################################################
# # matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# sum=0
# for row in range (len(matrix)):
#    for coloum in range(len(matrix(row))):
#       if(row==coloum):
#          sum=sum+coloum
#          print(sum)

# sum=0
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for x in range(len(matrix)):
#    sum=sum+matrix[x][x]
# print(sum)
########################################################################
sum=0
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ]
n=len(matrix)
print("total length of diagonal:", n)
for i in range(len(matrix)):
    sum=sum+matrix[i][n-1-i]
print("Sum of right to left diagonal sum is:", sum)


# 00  01  02
# 10  11  12
# 20  21  22

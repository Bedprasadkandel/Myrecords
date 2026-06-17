# #lambda function
# square=lambda x: x**2
# print(square(5))
# #next method:
# add=lambda a,b: a+b
# # print(add(3,4))

#map()
# numbers=[1,2,3,4,5,6]
# squared= list(map(lambda x:x**2,numbers))
# print(squared)

#normal function approach
# numbers=[1,2,3,4,5,6]
# def sq(x):
#     return x**2
# new_numbers=list(map(sq,numbers))
# print(new_numbers)
#2.filter########################
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_number=list(filter(lambda x:x%2==0,numbers))
# print(even_number)
#2 b.normal function
# numbers=[1,2,3,4,5,6,7,8,9,10]
# def even(x):
#     return x%2==0
# even_number=list(filter(lambda x:x%2==0,numbers))
# print(even_number)

# 
### reduce()
# example.1: summing up a list of numbers
from functools import reduce
# numbers=[1,2,3,4,5,6]
# sum=reduce(lambda x,y:x+y,numbers)
# print(sum)
#Example 2: Findingg the maximum number in a list

# numbers=[3,8,1,6,2]
# max_num=reduce(lambda x, y:x if x>y else  y, numbers)
# print(max_num)
# Example 3: Concatenating steings in a list

# words=reduce["Hello"," ", "world", "!"]
# sentence=reduce(lambda x, y: x+y, words)
# print(sentence)

##########################################
# import os
# current_dir= os.getcwd()
# print(current_dir)

# files=os.listdir(current_dir)
# print(files)


#Random############################
# Generate a random integer netween 1  and 10
# import random
# random_number= random.randint(1,10)
# print(random_number)
# #shuffle a list########################
# import random
# my_list=[1,2,3,4,5]
# random.shuffle(my_list)
# print(my_list)

import math
#trigonometric functions
print("exp(1):", math.exp(1))
print("log(e):",math)

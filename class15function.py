####function class supporting coding after 
# ###None type:
# x=None
# y=None
# print(x is)
################function program type 1:parameter less and non return type:
# def addition():
#     num1=int(input("enter num1:"))
#     num2=int(input("Enter num2:"))
#     result=num1+num2
#     print(result)
# addition()    
  
  ### type 3: with parameter and non return type
# def addition():
#     num1=int(input("enter num1:"))
#     num2=int(input("Enter num2:"))
#     result=num1+num2
#     return result

# final_result=addition() #### starting point to call def addition then comed from returned to  this line Addition()
# print(final_result)


## type4: with parameter and return type
#
# def addition(x,y):
#     result=x+y 
#     return result
# num1=int(input("enter num1:"))
# num2=int(input("enter num2:"))
# final_result= addition(num1,num2)
# print(final_result)



###########################################################################################

# def addition(num1, num2): ## we can call in various place
#     return num1 + num2

# def subtraction(num1, num2):
#         return num1 - num2
   

# def division(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 / num2

# def multiplication(num1, num2):
#     return num1 * num2


# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# while True:
#     symbol = input("""
# Choose operation (1,2,3,4,5)
# 1) Addition
# 2) Subtraction
# 3) Division
# 4) Multiplication
# 5) Exit

# Enter choice: """)

#     if symbol == "1":
#         print("Addition:", addition(num1, num2))

#     elif symbol == "2":
#         print("Subtraction:", subtraction(num1,num2))

#     elif symbol == "3":
#         print("Division:", division(num1, num2))

#     elif symbol == "4":
#         print("Multiplication:", multiplication(num1, num2))

#     elif symbol == "5":
#         print("Thank you!")
#         break
#     else:
#         print("Invalid choice")


################################################multiple vaariable of value can be  return
# def cal(x,y):
#     result1=x+y
#     result2=x-y
#     result3=x*y
#     return result1,result2,result3
# num1=int(input("Enter num1:"))
# num2=int(input("Enter num2:"))
# final_result=cal(num1,num2) 
# print(final_result)  
############################################################ used of list in by function
def cal(x, y):
    result = []
    result1 = x + y
    result2 = x - y
    result3 = x * y

    result.append(result1)
    result.append(result2)
    result.append(result3)

    return result

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

final_result = cal(num1, num2)
print(final_result)
################################## used  of tuple in function
# def get_stats(numbers):
#   min_value=min(numbers)
#   max_value=max(numbers)
#   sum_value=sum(numbers)
#   return min_value,max_value,sum_value


# ####Calling function:
# numbers=[1,2,3,4,5,6]
# min_val,max_val,total_sum=get_stats(numbers)
# print("Minimum:", min_val)
# print("Maximum:", max_val)

# print("Sum:", total_sum)

########################################################

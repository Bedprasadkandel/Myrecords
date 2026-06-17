#identity oprator:
# # is vs== is assign location in memory of variable.() 

#number1=[1,2,3,4]
#number2=[1,2,3,4]
# print(number1 is number2)

# num1=[1,2,3]
# num2=num1
#print(num1)
#print(num2)
#print (num1 is num2) #  value store location is same for num1 and num2

#6.Assignment operator:
# number = 60
# number=number+5
#number += 5
#number -= 5
#number *= 10
#number /= 10
#number %= 10
#number //= 10

# print(number)

# # Example of data type 

# x=("Hello world")
# print (type (x))  #str data type 

# num= 10
# print(type (num))    #integer data type 

# x= 20.5
# print(type (x))  # float data type

# y=2+1J           # complex data type
# print (type (y))

# x=["apple","banana","cherry"] #list data type
# print(type (x))

# x=("apple","banana","cherry") # tuple data type
# print(type (x))

# x=range(6)  #Range data type 
# print(type (x))

# x={"apple","banana","cherry"}   # set data type 
# print (type (x))

# x={"name":"john", "age" : 36 } # dic data type 
# print (type (x))

# x=frozenset ({"apple","babana","cherry"})      # frozenset data type
# print (type (x))
#x=True
#print (type(x))     #bool data type
 
#x = None
#print (type(x))     # None type data type.

# finisted of all data type
#number1=input("Enter first number:")
#number2=input("Enter the second number:")
#result=number1 + number2
#print ("Sum of two number result is :",result)

# type casting:

#1.integer to float
# num=50
# value=float(num)
# print("Change  the value form integer to float:", value)
# #2.integer to string
# num=50
# value  =str(num)
# print("integer value is change into string:",value)
# print(type(value )) #for checking data type

# #3 change data type float to integer 
# num=50.6
# value=int(num)
# print("The data type  is changed from float to integer:", value)

# #4. change data type  float to string 
# num=40.6
# name=str(num)
# print("The data type is changed from float to string:", name)
# print(type(name))

# #5.  Data type change from sting to integer 
num="30"
value=int(num)
print("change the data type from string to integer:",value)

#6. Data type change from sting to float
num="40"
value=float(num)
print("Change the data type from sting to float:",value)
# # finished

#first method:
number1=int(input("Enter first number:"))
number2=int(input("Enter the second number:"))
result=number1 + number2
print ("Sum of two number result is :",result)

# second method
number1=input("Enter first number:")
number2=input("Enter the second number:")
result=int(number1) + int(number2)
print ("Sum of two number result is :",result)



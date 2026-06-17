# A="NOHTYP" 
# for i in range(0,len(A)):
#     for j in range(i,-1,-1):
#         print(A[j],end="")
#     print()
#string:

# name="its a sunny day. \n It s rainly day"
# print(name)
# #new
# name="""abc
# def
# ghi
# """
# print(name)
# #new

# indexing:
# s="Hello, world!"
# print(s[0])
# print(s[7])
# print(s[4])
# print(s[5])
# print(s[6])
# print(s[7])
# print(s[8])
# print(s[9])
# print(s[10])
# print(s[11])
# print(s[12])
# Negative index
# s="Hello, world!"
# print(s[-1])
# print(s[-2])
# print(s[-3])
# print(s[-4])
# print(s[-6])

#slicing:
# s= ("Hello, world!")
# print((s[:5:2]))

# s="Hello, world!"
# print(s[7:12])
# # Next method of slicing




#Slicing steps:
# s="Hello, world!"
# print(s[::2])
# # print(s[7])

# s="Hello, world!"
# print(s[:5:2])

#new question:
# name="hello world"
# for x in name:
#     print(x)# output:"Hello world"

# print(len(name))

# index=0
# name="hello  world"
# for x in name:
#     print(x,":",index)
#     index=index+1
# print(len(name))

# name="hello world"
# for i in range(len(name)):
#     print(name[i], ":",i)
# New Question
# i=0
# name="hello world"
# while(i<len(name)):
#     print(name[i], ":",i)

#     i=i+1

################## pratice of room 


# name="it's a book" 
# print (name)

# name="it\'s a sunny day, It's a running day"
# print(name)

# s="HELLO, world"
# # print(s[:5:2])
# A=(s[:5])
# print(A[::2])
    

# num=str(input("Enter any character:"))
# rev=''
# for i  in num:
#     rev=i+rev
# if num==rev:
#     print("Yes , string  is palendrum")
# else:
#     print("No,string is not palendrom")



# a=input("Enter string:")
# b=a[-1::-1]
# if(a==b):
#     print("yes,palindrome string")
# else:
#     print("not,palindrome string:")

# #  write a program to check  user input number is  prime number or not.

# num=int(input("Enter the any number:  "))
# for i in range(2, num):
#     #print(i)
#     if num%i == 0:
#         print(num, "not a prime number")
#         break # To get  first any dividing number then termenating loop by break condititon:
      
# else:
#     print(num," is prime number")



# s = "Bed prasad kandel"
# print(s[0]) 
# print(s[4:10])
# print(s[:3])
#print(s[11:])
# print(s[::2])
# print(s[0:17:2])

# index=0
# name= "Hello world"
# for i in (name):
#     print(i,"=",index)
#     index=index+1
#     print("Total length:",len(name))
    

# a=str(input("Enter the number:  "))
# b= a[-1::-1]
# if(b==a):
#     print(" Given number is palindrome")
# else:
#     print("Given number is not palindrome ")
    

#Immutable data type:

# s="Hello"
# s[0]="h"#  this will raise a typeerror

s= "Hello"
s= "h"+ s[1:]
print(s)

# s= "Hello"
# s= "h"+ s[1:]+" " "python"
# print(s)

#String methods:

#1.replace():
# s="Hello world!"
# print(s.replace("world", "python"))
# print(s)

# #2.lower()
# s="Hello world!"
# print(s.lower())

# #3.upper():
# s="Hello world!"
# print(s.upper())
# #4.title:

# s="hello world!"
# print(s.title())



# s=" Hello, world! "
# print(s.lstrip())


# s="  Hello, world!  "
# print(s.rstrip())

# s=" Hello, world! "
# print(s.strip())

# s="#####!#### Hello python#######A###"
# print(s.strip("#!A"))



# s="Hello-python"
# value=s.split("-")
# print(value)

# input_value=['Hello', 'python']
# s="#".join(input_value)
# print(s)

#format string
# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# result=num1+num2

# print("result of {} and {}:". format(num1,num2),result)


#f_string:
# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# result=num1+num2

# print(f"result of {num1} and {num2}:",result)

#class_work
# question="#$%#$%#$%#$%@#$%HELLOWORLD@#$%@#$%@#$%"

# s= "$%#$%#$%#$%@#$%HELLOWORLD@#$%@#$%@#$%"
# print(s.strip("@#$%"),s.title())

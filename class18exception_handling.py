# num1=int(input("Enter your  num1:"))
# num2=int(input("Enter your number:"))
# result=num1/num2
# print(result)


# Type 1 : Raise inbuild Exception to handel different cases with different Except block
try:
    x=int(input("Enter the number first"))
    y=int(input("Enter the number second"))
    result= x/y
    print("Result",result)

except ZeroDivisionError as e:
    print(e)
    print("You have enter the zero value for number second")
    x=int(input("Enter the first number"))
    y=int(input("Enter the second  number"))
    result=x/y
    print("result",result)
except TypeError as e:
    print(e)
    print("You have enter the character instead of number")
    x=int(input("Enter the first number"))
    y=int(input("Enter the second number"))
    result=x/y
    print("result",result)
    
# Type 2: Raise inbuild Exception to handel different cases with same Except block

# try:
#     x=int(input("Enter the number first::"))
#     y=int(input("Enter the number second::"))
#     result= x/y
#     print("Result","=",result)

# except Exception as e:
#     print(e)
#     x=int(input("Enter the first number::"))
#     y=int(input("Enter the second number::"))
#     result=x/y
#     print("result","=",result)

# #Type3-Error Raise custom Exception to handel different cases with same Exceot block 
# try:
#         x= int(input("Enter the age:  "))
#         if x>100:
#             raise Exception("Sorry, no number above 100")
#         elif x==0:
#            raise Exception("Sorry, age is zero")
#         print(f"my age is {x}")
# except Exception as e:
#     print(e)
#     x=int(input("Re-Enter the age:  "))
#     print(f"my age is  {x}")
# ################# 
# class negative_error(Exception):
#      def __init__(self, message):
#           super().__init__(message)
# class zero_error(Exception):
#      def __init__(self,message):
#           super().__init__(message)
# x= int(input("enter the age"))
# try:
#      if x<0:
#           raise negative_error("Sorry, no number below zero")
#      elif x==0:
#           raise zero_error("Sorry, age is zero")
     
# except negative_error as e:
#      print(e)
#      print("you have enter the negative number")
#      x=int(input("Re- Enter the age"))
# except zero_error as e:
#      print(e)
#      print("Please enter the age based on month")
#      x=int(input("Enter the age based on month"))
# ###################################
# import traceback
# def divide():
#      print("Hello before try except")
#      try:
#           x=int(input("Enter the number for x"))
#           y=int(input("Enter the number for y"))
#           result=x/y
#           print("result",result)
#      except Exception as e:
#           traceback.print_exc()
#           print(f" handle all exception {e} ")
#########################################################
     
# import traceback
# def divide():
#     print("Hello before try except")

#     try:
#         x = int(input("Enter the number for x: "))
#         y = int(input("Enter the number for y: "))
#         result = x / y
#         print("Result:", result)

#     except Exception as e:
#          traceback.print_exc() # prints detailed error information
#          print(f"Handled exception: {e}")

#     divide()#### function call ho yo
##Create a list of five elements. Ask the user for an index and display the element at that index. Handle the exception when the index is out of range.

# items = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

# try:
#     index = int(input("Enter an index (0-4): "))
#     print("Element at index", index, "is:", items[index])

# except IndexError as e:
#     print(e)
#     index = int(input("Enter an index (0-4): "))
#     print("Element at index", index, "is:", items[index])

#    # print("Error: Index is out of range.")
    

# except ValueError as e:
#     print(e)
#     index = int(input("Enter an index (0-4): "))
#     print("Element at index", index, "is:", items[index])
   # print("Error: Please enter a valid integer.")
     ######################################################################
        
# Dictionary Key Error
# Create a dictionary of student records.
# Ask the user for a student's name and display the details.
# Handle the exception if the name is not found. 
students = {
    "Ram": {"Roll": 1, "Grade": "A"},
    "Sita": {"Roll": 2, "Grade": "B+"},
    "Hari": {"Roll": 3, "Grade": "A+"}
}

try:
    name = input("Enter student name : ")

    # Access the student's record
    details = students[name]

    print("Student Details:")
    print("Roll No:", details["Roll"])
    print("Grade:", details["Grade"])

except KeyError as e:
    print(e)
   # print("Error: Student name not found in the records.")
    name = input("Enter student name : ")

    # Access the student's record
    details = students[name]

    print("Student Details:")
    print("Roll No:", details["Roll"])
    print("Grade:", details["Grade"])


####Create a custom exception called AgeError. Raise it if the user's age is less than 18.
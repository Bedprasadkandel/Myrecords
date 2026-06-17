#chain condition:
num=55
if num>0:
    print("positive")
elif num<10:
    print("number less then 10")
# both conditon is true but given priorities for first condition

num=5
if num>0:
    print("this is positive number")

if num<10:
    print("All number is less then 10")
# Both if conditon are priented same time but  doesnot dependent to each other:

#Nested condition:
x=1
if x>0:
    if x<10:
        print("x is a positive single digit number")
    else:
        print("x is a positive ,but not a single_digit")
else:
    print("x is not a positive")

#question: Take input from user then converted integer to integer, float to float and c and character to character:
value=input("Enter any number")
if value .isdigit():
    value=int(value)
    print(value,"Converted into integer number:")
elif "." in value:
    value=float(value)
    print(value,"converted into float number")
else:
    print(value,"This is converted into string")

# next method:

value = input("Enter the any number:")
if value.isdigit():
    value=int(value)
    print("converted to integer:")
elif"." in value:
    value=float(value)
    print("converted to float")
else:
    print("converted to string")
            


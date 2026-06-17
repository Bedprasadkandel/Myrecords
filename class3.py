# #condition
# #IF casle
# #method using only if
# # num= int(input("Enter the number:"))
# # if num==10:
# #  print("the number is 10")

# #method 2. using if-else
# # num=int(input("Enter the number"))
# # if num==10:
# #  print("the number is 10")
# # else:
# #  print("invalid number please enter number 10")
        
#  #method3:using if elif

# # num=int(input("Enter your number"))
# # if num==20:
# #     print("the number is 20")
# # elif num==30:
# #     print("the number is 30")
# # elif num==40:
# #     print("the number is 40")
# # Question1:take user input and check if number is odd or even

# # num= int(input("Enter the number"))
# # if num%2==0:
# #     print("the number is even number")
# # else:
# #     print("the given number is odd")
    
# #take a user  input and  check if number is positive or negative  or zero

# # num=int(input("Enter your number"))
# # if num<0:
# #     print("the number is negative")
# # elif num>0:
# #     print("the number is positive")
# # elif num==0:
# #     print("the number is Zero")

num=str(input("Enter the any character:"  ))
if "a" in num or "e" in num or "i"in num or "o" in num or  "u" in num:
   
   print("This latter is vobel letter")
else:
   print("This is not vobel letter")

# #3.Take user input and check if user input string has lowel character in it or not
# num=str(input("Enter the  any character "))
# if "a"in num :
#     print("a is involve in given input string ")
# elif "e" in num:
#     print("e is involve in given input string")
# elif "i" in num:
#     print("i is involve in given  input string")
# elif "o" in num:
#     print("o is involve in given inpit string")
# elif "u" in num:
#     print("u is involve in given  input string ")
# else:
#     print("not involve in given string in vowel letter")

# #4.Take three numbers from user and print the highest number among three number?
 
# # a=int(input("Enter first  number"))

# # b=int(input("Enter second  number"))
# # c=int(input("Enter third  number"))
# # if a>b and a>c:
# #     print("a is histest number")
# # elif b>a and b>c:
# #     print("the number b is greater then other number:")
# # elif(c>a and c>b):
# #     print("The number is c is largest")
# # else:
# #     print("no one  is greater then ")

# #5. Give option to user i.e +,-,*,/ if user enter any symbol perform arithmatic operation based on that for two numbers.
# # num1=int(input("Enter first  number"))
# # num2=int(input("Enter second  number"))
# # symbol=str(input("Choose any symbol (=, +, -, %, *, /)"))

# # if "+" == symbol :
# #   add=num1+num2
# #   print("Addition of two number is:",add)

# # elif "-" == symbol:
# #    sub=num1-num2
# #    print("Subtraction between two number is:", sub)

# # elif "*" == symbol:
# #    multi=num1*num2
# #    print("MUltiplication of two number is :", multi)
   
# # elif "%" == symbol:
# #    div=num1 % num2
# #    print("Result of division is :", div)

# # elif "=" ==symbol:
# #    equal=num1==num2
# #    print("num1 is equal to num2:",equal)

# # elif "/" == symbol:
# #    mod=num1/num2
# #    print("modules of two number result is :",mod)

# # else:
# #     print("Right option was not choosen :")

# #Method6: Create the grade system take  user input and Determine A+,A,B+,B,C+,c.

# score =int(input("Enter  number"))
# if score >= 90:
#   print("Grade: A+")
# elif score >= 80:
#   print("Grade: A")
# elif score >= 70:
#   print("Grade: B+")
# elif score >= 60:
#   print("Grade: B")
# elif score >= 50:
#   print("Grade: c+")
# elif score >= 40:
#   print("Grade:C")
# else:
#   print("NG")

# #7.Take a user input and check if number is Divisible by 5 and 11.

# # num = int(input("Enter a number: "))
# # # Check divisibility by 5 and 11
# # if num % 5 == 0 and num % 11 == 0:
# #     print(num, "is divisible by both 5 and 11")
# # else:
# #     print(num, "is not divisible by both 5 and 11")


# #8.Take user input in farnheit or celsuit and convert to vice versa.

# choice = input("Convert from Celsius or Fahrenheit? or farhenheit to celsius chose any character C or F: ")

# if choice == 'C' or choice == 'c':
#     celsius = float(input("Enter temperature in Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print("Temperature in Fahrenheit =", fahrenheit)

# elif choice == 'F' or choice == 'f':
#     fahrenheit = float(input("Enter temperature in Fahrenheit: "))
#     celsius = (fahrenheit - 32) * 5/9
#     print("Temperature in Celsius =", celsius)

# else:
#     print("Invalid choice!")
# #continue:
# # for x in range(10):
# #     if x==5:
# #         continue
# #     print(x)

# # for x in range(10):
# #     if x==5:
# #         break
# #     print(x)

# #user input sum all user input 0 exit and print toal sum,  50 skip to add in sum
# # x=0
# # sum=0
# # while(x==0):
# #     value=int(input("Enter the any number")) #20,50
     
# #     if value==0:
# #         print(sum," is sum number of input")
# #         break
# #     if value==50:
# #             continue
# #     sum=sum+value #sum =20+ 50 = 70

# # while True:
# #     print("""
# #     Enter your choice:
# #           1.Addition
# #           2.substraction
# #           3.Division
# #           4.multiplication
# #           5.Exit
# #           """)
# #     choice=int(input("enter your choice from above:"))
# #     if choice==5:
# #        print("Existing.........")
# #        break # Break mean stoping the program:

# #     num1=int(input("Enter your number1:"))
# #     num2=int(input("Enter your number2:"))

# #     if choice==1:
# #         print("The sum of two number is:", num1+num2)

# #     elif choice==2:
# #         print("The Different of two number is:", num1-num2)

# #     elif choice==3:
# #         print("The division of two number is:", num1 % num2)

# #     elif choice==4:
# #         print("The multiplication  of two number is:", num1 * num2)
        




# # # while True:
# # #     print("""
# # #     Enter your choice:
# # #           1.Addition
# # #           2.Subtraction
# # #           3.Division
# # #           4.Multiplication
# # #           5.Exit
# # #     """)

# # #     choice = int(input("Enter your choice from above: "))

# # #     if choice == 5:
# # #         print("Exiting.........")
# # #         break

# # #     num1 = int(input("Enter your number1: "))
# # #     num2 = int(input("Enter your number2: "))

# # #     if choice == 1:
# # #         print("Sum:", num1 + num2)

# # #     elif choice == 2:
# # #         print("Difference:", num1 - num2)

# # #     elif choice == 3:
# # #         print("Division:", num1 / num2)

# # #     elif choice == 4:
# # #         print("Multiplication:", num1 * num2)

# # #     else:
# # #         print("Invalid choice")
        





            
#    # Write a Python program to print numbers from 1 to 10 using break when the number becomes 6.
# num=10
# for i in range(num):
#     # print(i)
#     if i==6:
#         break
#     print(i)
# #Write a Python program to print numbers from 1 to 10 but skip number 5 using continue.
# # num=10
# # for i in range(num):
# #     if i==5:
# #         continue
# #     print(i)
        
# #Write a Python program that asks the user to enter numbers continuously and stops when the user enters 0 using break.

# # while True:
# #     sum=0
# #     num = int(input("Enter any number continuously: "))

# #     if num == 0:
# #         print("Exiting the program............................?")
# #         break

# #     elif num > 0:
# #         print("Continue to operate a program .......")

# #Write a Python program to print all odd numbers from 1 to 20 using continue.

# # for num in range(1 , 21):

# #     # if num%2 !=0:    # skip by continues all odd number 
# #     if num%2==0:
# #         continue       # Skip by continues all even number 
# #     print(num)
# #Write a Python program that checks each letter of a word and stops the loop when the letter a is found using break.
# # 
# # word = str(input("Enter a word: "))

# # for letter in word:

# #     if letter == 'a':
# #         print("Letter 'a' found")
# #         break

# #     print(letter)

# while Test:
#     number=int(input("Enter the number"))
#     if number<0:
#         print("this number is negative")
#         continue

#     elif number==0:
#         print("Stop the program")
#     break
# print("Square=", number*number)
# 2. Password Check Using Break

# Write a program that:
# Gives the user 3 chances to enter the correct password "python123"
# If the password is correct, print "Access Granted" and stop the loop using break
# If all attempts fail, print "Access Denied"

# correct_password="python123"
# for i in range(3):
#     correct=input("Enter the correct password:")
#     if correct_password==correct:
#         print("the password is correct, print Access Granted:")
#         break
#     else:
#         print("Wrong password:")
# else:
#      print("Access Denied:")

# #############################################################
# . Guess the Number Game

# Write a program where:

# The secret number is 7
# The user keeps guessing
# If the guess is correct, print "Correct!" and stop using break
# Otherwise keep asking

# secret = 7
# count = 0

# while True:
#     match = int(input("Enter the secret number: "))

#     if match == secret:
#         print("Correct!")

#         count += 1
#         break
#     else:
#         print("Incorrect please try again")

#     count += 1  # counts every attempt

#     print("Total attempts:", count)

# #################################################################
# Find First Negative Number

# Write a program that:

# Takes a list of numbers from the user
# Prints numbers one by one
# Stops printing when it finds the first negative number using break

new_list = []

while True:
    number = int(input("Enter the number: "))

    if number > 0:
        new_list.append(number)
        print("Element added successfully")
        print("Current list:", new_list)  # Print after adding
    else:
        print("Please enter a positive number.")
        break  # Stop when a non-positive number is entered

print("Final list:", new_list)
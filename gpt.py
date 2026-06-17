# try:
#         x= int(input("Enter the first number::"))
#         y=int(input("Enter the second number::"))
#         z=x/y
#         print("result",z)
# except ZeroDivisionError as e:
#         print(e)
#         x= int(input("Enter the first number::"))
#         y=int(input("Enter the second number::"))
#         z=x/y
#         print("result",z)
#         print("This is Zero division Error")
# except TypeError as e:
#         print(e)
#         x= int(input("Enter the first number::"))
#         y=int(input("Enter the second number::"))
#         z=x/y
#         print("result",z)
#         print("This is type Error::")
# except ValueError as e:
#         print(e)
#         x= int(input("Enter the first number::"))
#         y=int(input("Enter the second number::"))
#         z=x/y
#         print("result",z)
#         print("This is valueError Error::")
# finally:
#         print("End of program::")

##Create a list of five elements. Ask the user for an index and display the element at that index. Handle the exception when the index is out of range.

items = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

try:
    index = int(input("Enter an index (0-4): "))
    print("Element at index", index, "is:", items[index])

except IndexError:
    print("Error: Index is out of range.")

except ValueError:
    print("Error: Please enter a valid integer.")
        
 

#creating a list of integers
# number=[1,2,3,4,5]
# print(number[2])              #answer:3
# # ##creating a list of string
# fruits=['apple','banana','cherry','orange']
# print(fruits[1:3])            # answer=banana,cherry

# # #creating a a mixed-type list
# mixed_list=[10,'hello',True, 3.14]
# print(mixed_list[2])          #answer=true


# lst=[1,2,3,4,"abc",1.5]
# for x in lst:
#     print(x)
# lst=[1,2,3,4,"abc",1.5]
# for i in range(len(lst)):
#     print(lst[1:5])

                                                  #Modifing the list:
# fruits=['apple','banana','cherry','orange']
# fruits[0]="mango"
# print(fruits)

                                                    #Adding the element in last place of  list
# fruits=['Banana','orange','mango']
# fruits.append('Apple')
# print(fruits)
                                             #insert element in your requirement placement:

# fruits=['Banana','orange','mango']
# fruits.insert(1, 'Apple')
# print(fruits)

                                              #Removeing the element from list
# fruits=['orange','Banana','mango','apple']
# fruits.remove('orange')  
# print(fruits) 
                                            #Removing the element from pop operation way
# fruits=['Banana','orange','mango']
# fruits.pop(1)
# print(fruits)

                                           #Updating the element in list
# fruits=['orange','mango','apple']
# fruits[2]="banana"
# print(fruits)

# number.append(100)
# number.insert(1,100)

# #remove
# fruits=["apple","apple","banana","cherry"]
# fruits.remove("apple")
# fruits.pop(1)
# del fruits(0)
# del fruits[0]
# fruits.clear()
# #update

# fruits=["apple","apple","banana","cherry"]
# fruits[2]="pinepal"
# print(fruits)
# ###################################################################################
#######################################################################
# fruits = []

# while True:
#     print("""
#     Enter your choice:
#         1. Add
#         2. Update
#         3. Delete
#         4. View
#         5. Exit
#     """)
#     choice = int(input("Enter your choice from above: "))
#     if choice == 5:
#         print("Exiting.........")
#         break
#     elif choice == 1:
#         request = input("Enter the fruit name: ")
#         fruits.append(request)
#         print("Fruit added successfully.")
#         print(fruits)
#     elif choice == 2:
#         index = int(input("Enter fruit index to update: "))
#         update = input("Enter new fruit name: ")
#         if 0 <= index and index< len(fruits):
#             fruits[index] = update
#             print("Fruit updated successfully.")
#             print(fruits)
#         else:
#             print("Invalid index!")
#     elif choice == 3:
#         index = int(input("Enter fruit index of delete: "))
#         if 0 <= index and index < len(fruits):
#             deleted = fruits.pop(index)
#             print(deleted, "deleted successfully.")
#             print(fruits)
#         else:
#             print("Invalid index!")
#     elif choice == 4:
#         print("Fruit List:", fruits)
#     else:
#         print("Invalid choice!")
###################################################################################
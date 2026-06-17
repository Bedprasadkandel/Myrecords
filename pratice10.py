# ##### creating list
# # number=[1,2,3,'bed',1.4,'kandel']
# # print(number[5])
# # list=["banana","orange",'mango',"örange"]
# # print(list[0:3:2])

# # list=['orange','mango','apple','naspati']
# # list[1]='watermilon'
# # print(list)

# # list=["Hari","Bed","Bimala"]             # creating list
# # list.insert(1,"Gita")# inserting
# # list.remove("Bed")## removing
# # list[2]="Sita" ##Updating
# # list[0]="Laxman"#modifying
# # print(list)

          


# ##################################################### coding by teacher:
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
#       old_value=input("Enter your old value to be updated")
#       if old_value in fruits:
#           new_value=input("Enter your new value to be updated:")
#           for i in range(len(fruits)):
#              if fruits[i]==old_value:
#                 fruits[i]=new_value
#                 print("fruits is  updated sucessfully.....")  
#       else:
#             print("fruits to be updated not found..............")

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
################################################# coding in classwork 

    
####Question1: fruits=["Apple","apple","banana","orange","grapes","pine",]
#Answer: ["banana","orange","graps","pine"]
# TO take  user input to remove the item if duplicated is found deleted both:

fruits=["Apple","apple","banana","orange","grapes","pine"]
item = input("Enter fruit name to remove if duplicate found: ")
remove=[]
for x in fruits:
   if item.lower()==x.lower():
      remove.append(x)
 
for data in remove():
  fruits.remove(data)
  print(item,"this fruits is duplicated delete is sucessfully:")

# 

#Question2: fruits=["apple","apple","banana","orange","graps","pine","banana","banana"]
# result=["apple","banana","orange","graps","pine"]

# fruits=["apple","apple","banana","orange","graps","pine","banana","banana"]
# Result_fruits=[]
# for i in fruits:
#     if i not in Result_fruits:
#         Result_fruits.append(i)
# print(Result_fruits)

#item=["apple","ball","ct","dog","ft","ht"]
###remove item that have vowel character it
######################################################################

# item = ["apple", "ball", "ct", "dog", "ft", "ht"]
# vowels = "aeiou"
# result = []

# for world in item:          # Take one word at a time
#     has_vowels = False      # Assume no vowel

#     for letter in world:    # Check each letter in the word
#         if letter in vowels:
#             has_vowels = True
#             break

#     if not has_vowels:      # If no vowel found
#         result.append(world)

# print(result)

# fruits=["orange","mango","cucumber","banana","mango"]
# non_duplicated=[]
# for i in fruits:
#     if i not in non_duplicated:
#         non_duplicated.append(i)
# print(non_duplicated)
# fruit=["orange","mango","apple","banana"]
# fruit.append("pinepal")
# fruit.insert(1,'patato')

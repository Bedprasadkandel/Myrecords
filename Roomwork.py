# fruits=["Banana","Örange","mango","papaya","grapes","pinepal","cucumber"]
# # involve_alist=[]
# # for x in fruits:
# #     if "b"  not in x:
# #         involve_alist.append(x)
# print(involve_alist)

# involve_alist=[x for x in fruits if "a" in x ]
# print(involve_alist)


#Set classwork #########################################################
# letter={"A","B","C","D","E","F","G"}
# del letter
# print(letter)

#####################################################################################3
# total_number=int(input("How many mobile number is required:"))
# new_number=[]
# for i in  range(total_number):
#     while True:
#         mobile=(input(f"Enter a mobile number{i+1}:"))
#         if len(mobile)==10 and mobile.isdigit():
#             new_number.append(mobile)
#             break
#         else:
#             print("Invalid mobile number!, please enter number between 0 to 10:")

# print(new_number)

####################################################################################

# total_subject= int(input("How many  subjects number of mask need?:"))
# marks=[]
# sum=0
# for i in range(total_subject):
#     while True:
#      mark=float(input(f"Enter your subjects mask {i+1}:"))
#      if(0<=mark and mark<=100):
#         marks.append(mark)
#         sum= sum+mark
#         break
#      else:
#         print("please, Enter maske between 0 to 100:")
# print(marks)
# print(("Total subject masks is:"),
# with open("E:\pythonbroadway\demofile2.txt", mode="r") as file:
#    value= file.read()
#    value=value.replace("bed","Prem")
#    value=value.replace("person","my son")
#    value=value.replace("student","Teacher")
#    print(value)


# with open("E:\pythonbroadway\demofile2.txt",mode="r") as file:
#    # value=file.readline()
#    for row in file:
#         print(row)


# new_list=[]
# with open("E:\pythonbroadway\demofile2.txt",mode="r") as file:
#    value=file.readlines()
#    value=['my name is bed prasad kandel\n', 'i am honorable person\n', 'i am engineering student']
#    for index in value:
#       new_list.append(index.strip("\n"))
# print(new_list)
# print(new_list[2]) 
         








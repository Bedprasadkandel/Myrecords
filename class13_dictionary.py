#set method
#1.union set################################################
# set1={1,2,3,4}
# set2={1,2,5}
# set3=set1.union(set2)
# print(set3)
#  short form of union#################################################
# set1={1,2,3,4}
# set2={1,2,5}
# set4={6,7}
# set3=set1| set2| set4
# print(set3)
#.union update:############################################
# set1={1,2,3,4}
# set2={1,2,5}
# set3=set1.union(set2)
# set1.update(set2,set3)
# print("Updated result of set1:", set1) aaba new set1 create vayo
#2.intersection:##########################################################

# set1={1,2,3,4}
# set2={1,2,}
# set3={1,2,7}
# # set4=set1.intersection(set2,set3)
# set4=set1 & set2 & set3 # short form of intersection
# print(set4)

# #3.intersection update##########################################################
# set1={1,2,3,4}
# set2={1,2,6}
# set3={1,6}
# set4=set1.intersection_update(set2,set3)
# set4=set1 & set2 & set3
# print(set4)

#difference###########################################
# set1={1,2,3,4}
# set2={1,2,5}
# set3=set1.difference(set2)
# set3=set1-set2
# print(set3)
#difference update##########################################
# set1={1,2,3,4}
# set2={1,2,5}
# set3=set1.difference_update(set2)
# set3=set1-set2
# print(set3)
#symmetric difference#####################################
# set1={1,2,3,4}
# set2={1,2,5}
# set3=set1.symmetric_difference(set2)
# set3=set1^set2
# print(set3)
#symmetric difference update############################################
# set1={1,2,3,4}
# set2={1,2,5}
# set3=set1.symmetric_difference_update(set2)
# set3=set1^set2
# print(set3)

#dictionary ### important data types #############################################
# empty_dict={}
# my_dict={
#     "name": "Alice",
#     "age": 30,
#     "city":"new work"    
# }
# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["city"])
# print(my_dict.get("age"))

####################################
# my_dict={
#     "name": "Alice",
#     "age": 30,
#     "city":"new work"    
# }
# my_dict["age"]=31
# my_dict["Gender"]="male"
# print(my_dict)


# mixed_dict={
#     1: "one",
#     "2":"two",
    # (1,2,): "tuple"
# }
#modifying and adding element####################################
# empty_dict={}
# my_dict={
#     "name": "Alice",
#     "age": 30,
#     "city":"new work"    
# }
# print(my_dict["age"])
# my_dict["gender"]="female"    #######################Adding new data in dictionary:
# print(my_dict)
############################################
# del my_dict["city"]
# my_dic.pop


#loop######################### 
# data={
#    "name":"ram",
#    "roll":12
#  }
# for x in data:
#     print(x)
#next method############################
# data={
#    "name":"ram",
#    "roll":12
#  }
# for x in data.keys():
#     print(x)
    #####################################
# data={
#    "name":"ram",
#    "roll":12
#  }
# for value in data.values():
#    print(value)
   #############################

# data={
#    "name":"ram",
#    "roll":12
#  }
# for k,v in data.items():
#     print(k,":",v)

# ################################
# data={
#   "name":"ram",
#   "roll":12
#   }
# for x in data:                                    

#   print(x, ":",data[x])
##########################################################################################

### Dictionary problem in python:
# my_details={
#     "Name":"Bed prasad kandel",
#    "Address":"Palpa",
#     "Age":30,
#     "City": "Rampur munucipility",
#      "Percentage":"72%",
#      "Gender":"male"
# }
# for key, value in my_details.items():
#  print(key, ":", value)
  
##########################################################################################  Better  program as compare below 
# Name = input("Enter your name: ")
# Roll_No = int(input("Enter your roll NO: "))
# Address = input("Enter your Address:")
# total_subject = int(input("How many subjects? "))
# marks = []
# total_marks = 0
# for i in range(total_subject):
#     while True:
#         mark =float(input(f"Enter marks of subject {i+1}: "))
#         if 0 <= mark and mark <= 100:
#             marks.append(mark)
#             total_marks= total_marks + mark
#             break
#         else:
#             print("Marks must be between 0 and 100.")
# total_number = int(input("How many mobile numbers: "))
# new_number = []


# for x in range(total_number):
#     while True:
#         mobile = input(f"Enter mobile number {x+1}: ")
#         if len(mobile) == 10 and mobile.isdigit():
#             new_number.append(mobile)
#             break
#         else:
#             print("Mobile number must be exactly 10 digits.")
# student={
# }
# student["Name"]=Name
# student["Roll_no"]=Roll_No
# student["Address"]=Address
# student["mark"]=marks
# student["Total_marks"]=total_marks
# student["Contract"]=mobile
# print("Total records of students:",student )

    


############################################################################################################### 
# Name = input("Enter your name: ")
# Roll_No = int(input("Enter your roll NO: "))
# Address = input("Enter your Address:")
# total_subject = int(input("How many subjects? "))
# marks = []
# total_marks = 0
# for i in range(total_subject):
#     while True:
#         mark =float(input(f"Enter marks of subject {i+1}: "))
#         if 0 <= mark and mark <= 100:
#             marks.append(mark)
#             total_marks= total_marks + mark
#             break
#         else:
#             print("Marks must be between 0 and 100.")
# total_number = int(input("How many mobile numbers: "))
# new_number = []


# for x in range(total_number):
#     while True:
#         mobile = input(f"Enter mobile number {x+1}: ")
#         if len(mobile) == 10 and mobile.isdigit():
#             new_number.append(mobile)
#             break
#         else:
#             print("Mobile number must be exactly 10 digits.")
# student={
#     "Name":Name,
#     "Roll_no":Roll_No,
#     "Address":Address,
#     "mask":marks,
#     "Total_masks":total_marks,
#     "Contract":mobile    
# }  
# print(">>>>>>>>>>>>>>This is record of students>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# for key, value in student.items():
#     print(key, ":", value)
    



###########################################################################################################
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

###########################################################################
####Write a  program should be  mask is only positive between 0 to 100. if negative masks and  above 100 maske should be error occur?

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
# print(("Total subject masks is:"),sum)

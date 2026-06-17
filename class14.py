# ## #######################this right procedure 1. program looping  system program  for multiple user
# students={}
# total=int(input("How many time do you need?"))

# for student_records in range(1,total+1):
#     Name = input("Enter your name: ")
#     Roll_No = int(input("Enter your roll NO: "))
#     Address = input("Enter your Address:")

#     total_subject = int(input("How many subjects? "))
#     marks = []
#     total_marks = 0
#     for i in range(total_subject):
#      while True:
#             mark =float(input(f"Enter marks of subject {i+1}: "))
#             if 0 <= mark and mark <= 100:
#                 marks.append(mark)
#                 total_marks= total_marks + mark
#                 break
#             else:
#                 print("Marks must be between 0 and 100.")
#     total_number = int(input("How many mobile numbers: "))
#     new_number = []


#     for x in range(total_number):
#         while True:
#          mobile = input(f"Enter mobile number {x+1}: ")
#          if len(mobile) == 10 and mobile.isdigit():
#              new_number.append(mobile)
#              break
#          else:
#              print("Mobile number must be exactly 10 digits.")
#     student={
#         "Name":Name,
#         "Roll_no":Roll_No, ## dictionary 
#         "Address":Address,
#         "mark":marks,
#         "Total_marks":total_marks,
#         "Contract":new_number,
#     }
#     students[student_records] = student 
# print("\n All student Records:")
# print(students)
# ###################################### check highest marks of student: complete correct program

# students={
#     1:  {"name":"Ram",
#         "rollno":1,
#         "address":"ktm",
#         "marks" : [80,80,80,80],
#         "total_marks":320,
#         "contract":[9800752990,9800753554]
# },
# 2 : {"name":"Hari",
#         "rollno": 2,
#         "address":"Butwal",
#         "marks" : [90,90,90,90],
#         "total_marks":360,
#         "contract":[980075220,9800753890]    
# },

# 3 : {"name":"Bed",
#         "rollno": 3,
#         "address":"Pokhara",
#         "marks" : [70,70,70,70],
#         "total_marks":980,
#         "contract":[980075330,9800753440]    
# }
# }
# highest_value = 0
# highest_student = None

# for key, value in students.items():
#     if value["total_marks"] > highest_value:
#         highest_value = value["total_marks"]
#         highest_student = value

# print("Detail of highest marks student:")
# print(highest_student)

############################ or below code you can used option to above ##########################################
# highest_value = 0
# my_key = 0

# for key, value in students.items():
#     if value["total_marks"] > highest_value:
#         highest_value = value["total_marks"]
#         my_key = key

# print("Detail of highest marks student:",students[my_key])
# print(students[my_key])

################## Highest marks disaplay as Compare of student marks #################################### 


# students={}
# total=int(input("How many time do you need?"))
# for student_records in range(1,total+1):
#     Name = input("Enter your name: ")
#     Roll_No = int(input("Enter your roll NO: "))
#     Address = input("Enter your Address:")
#     total_subject = int(input("How many subjects? "))
#     marks = []
#     total_marks = 0
#     for i in range(total_subject):
#      while True:
#             mark =float(input(f"Enter marks of subject {i+1}: "))
#             if 0 <= mark and mark <= 100:
#                 marks.append(mark)
#                 total_marks= total_marks + mark
#                 break
#             else:
#                 print("Marks must be between 0 and 100.")
#     total_number = int(input("How many mobile numbers: "))
#     new_number = []


#     for x in range(total_number):
#         while True:
#          mobile = input(f"Enter mobile number {x+1}: ")
#          if len(mobile) == 10 and mobile.isdigit():
#              new_number.append(mobile)
#              break
#          else:
#              print("Mobile number must be exactly 10 digits.")

#     student={
#         "Name":Name,
#         "Roll_no":Roll_No, ## dictionary 
#         "Address":Address,
#         "mark":marks,
#         "Total_marks":total_marks,
#         "Contract":new_number,
#     }
#     students[student_records] = student 
# # print("\n All student Records:")
# # print(students)

# highest_value = 0
# highest_key = None

# for key, value in students.items():
#     if value["Total_marks"] > highest_value:
#         highest_value = value["Total_marks"]
#         highest_key = key
# print(">>>>>>>>>>>>>>>>>>>>>>>Highest marks student records of students<<<<<<<<<<<<<<<<<<<<<<<<<")
# print("Student Record No:", highest_key)
# print("Student Details:", students[highest_key])

################## Disply of students Details who get Total_marks more then 500 only  ######################

# students={}
# total=int(input("How many time do you need?"))
# for student_records in range(1,total+1):
#     Name = input("Enter your name: ")
#     Roll_No = int(input("Enter your roll NO: "))
#     Address = input("Enter your Address:")
#     total_subject = int(input("How many subjects? "))
#     marks = []
#     total_marks = 0
#     for i in range(total_subject):
#      while True:
#             mark =float(input(f"Enter marks of subject {i+1}: "))
#             if 0 <= mark and mark <= 100:
#                 marks.append(mark)
#                 total_marks= total_marks + mark
#                 break
#             else:
#                 print("Marks must be between 0 and 100.")
#     total_number = int(input("How many mobile numbers: "))
#     new_number = []


#     for x in range(total_number):
#         while True:
#          mobile = input(f"Enter mobile number {x+1}: ")
#          if len(mobile) == 10 and mobile.isdigit():
#              new_number.append(mobile)
#              break
#          else:
#              print("Mobile number must be exactly 10 digits.")

#     student={
#         "Name":Name,
#         "Roll_no":Roll_No, ## dictionary 
#         "Address":Address,
#         "mark":marks,
#         "Total_marks":total_marks,
#         "Contract":new_number,
#     }
#     students[student_records] = student 
# # print("\n All student Records:")
# # print(students)
# print(">>>>>>>>>>>>>>>>>>>>>>> Students with Total Marks > 500 <<<<<<<<<<<<<<<<<<<<<<<<<")

# found = False

# for key, value in students.items():
#     if value["Total_marks"] > 500:
#         print("\nStudent Record No:", key)
#         print("Student Details:", value)
#         found = True

# if not found:
#     print("No student has total marks greater than 500.")





#############  Display only top 5 student result details to request from user ###########################
students={}
total=int(input("How many time do you need?"))
for student_records in range(1,total+1):
    Name = input("Enter your name: ")
    Roll_No = int(input("Enter your roll NO: "))
    Address = input("Enter your Address:")
    total_subject = int(input("How many subjects? "))
    marks = []
    total_marks = 0
    for i in range(total_subject):
     while True:
            mark =float(input(f"Enter marks of subject {i+1}: "))
            if 0 <= mark and mark <= 100:
                marks.append(mark)
                total_marks= total_marks + mark
                break
            else:
                print("Marks must be between 0 and 100.")
    total_number = int(input("How many mobile numbers: "))
    new_number = []


    for x in range(total_number):
        while True:
         mobile = input(f"Enter mobile number {x+1}: ")
         if len(mobile) == 10 and mobile.isdigit():
             new_number.append(mobile)
             break
         else:
             print("Mobile number must be exactly 10 digits.")

    student={
        "Name":Name,
        "Roll_no":Roll_No, ## dictionary 
        "Address":Address,
        "mark":marks,
        "Total_marks":total_marks,
        "Contract":new_number,
    }
    students[student_records] = student 
# print("\n All student Records:")
# print(students)
top_n = int(input("How many top students do you want? "))
sorted_students = sorted(students.items(),
    key=lambda x: x[1]["Total_marks"],
    reverse=True
)
print("\n>>>>>>>> TOP 5 STUDENTS <<<<<<<<<<\n")
  # in case less than 5 students
top_n = int(input("How many top students do you want? "))

print("\n🏆 Top Students:")
for i, (key, student) in enumerate(sorted_students[:top_n], start=1):
    print(f"\nRank {i}")
    print(f"Name: {student['Name']}")
    print(f"Roll No: {student['Roll_no']}")
    print(f"Total Marks: {student['Total_marks']}")




################## Only display  who students has a addres of pokhara.##################
# students={}
# total=int(input("How many time do you need?"))

# for student_records in range(1,total+1):
#     Name = input("Enter your name: ")
#     Roll_No = int(input("Enter your roll NO: "))
#     Address = input("Enter your Address: ").strip().lower()

#     total_subject = int(input("How many subjects? "))
#     marks = []
#     total_marks = 0
#     for i in range(total_subject):
#      while True:
#             mark =float(input(f"Enter marks of subject {i+1}: "))
#             if 0 <= mark and mark <= 100:
#                 marks.append(mark)
#                 total_marks= total_marks + mark
#                 break
#             else:
#                 print("Marks must be between 0 and 100.")
#     total_number = int(input("How many mobile numbers: "))
#     new_number = []


#     for x in range(total_number):
#         while True:
#          mobile = input(f"Enter mobile number {x+1}: ")
#          if len(mobile) == 10 and mobile.isdigit():
#              new_number.append(mobile)
#              break
#          else:
#              print("Mobile number must be exactly 10 digits.")

#     student={
#         "Name":Name,
#         "Roll_no":Roll_No, ## dictionary 
#         "Address":Address,
#         "mark":marks,
#         "Total_marks":total_marks,
#         "Contract":new_number,
#     }
#     students[student_records] = student 

# print(">>>>>>>>>>>>>>>>>>>>>>> Students from Pokhara <<<<<<<<<<<<<<<<<<<<<<<<<")

# found = False

# for key, value in students.items():
#     if value["Address"].lower() == "pokhara":
#         print("\nStudent Record No:", key)
#         print("Student Details:", value)
#         found = True

# if not found:
#     print("No student found from Pokhara.")

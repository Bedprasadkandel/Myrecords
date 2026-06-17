# f=open("E:\pythonbroadway\demofile.txt",mode="r") ### f is variable
# value=f.read()
# print(value)
# f.close()

# f=open("E:\pythonbroadway\demofile.txt",mode="w")
# value=f.write()
# print(value)
# f.close()

##type:2
# with open("E:\pythonbroadway\demofile2.txt",mode="r") as file:
#     value=file.read()
#     value=value.replace("bed","Prem")
#     value=value.replace("honorable","lazy")
#     value=value.replace("engineering","management")
#     print(value)

# with open("E:\pythonbroadway\demofile.txt",mode="r") as w:
#     value=w.read()
#     print(value)
#############################
# with open("E:\pythonbroadway\demofile.txt",mode="r") as f:
#     value=f.read()
#     print(value)
#     print(value.replace("hello", "Hello ")

#     print(type(value))


# Approach 2: readline()
# with open("E:\pythonbroadway\demofile.txt",mode="r") as f:
    # value=f.readline()
    # print(value)
    # print(type(value))
    # line2=f.readline()
    # print(line2)
    # line3=f.readline()
    # print(line3)
#####Alternative method: for loop used
# with open("E:\pythonbroadway\demofile2.txt",mode="r") as f:
#     for row in f:
#         print(row)
#####approach 3:readlines()
# empty_list=[]
# with open("E:\pythonbroadway\demofile.txt", mode="r") as f:
#     value=f.readlines()
#     value=['Hello! Welcome to demofile.txt\n', 'This file is for testing purpose.\n', 'Good Luck!']
#     for index in value:
#      empty_list.append(index.strip("\n"))
# print(empty_list)
################write mode:
with open("E:\pythonbroadway\demofile.txt", mode="w") as f:
    value=f.write("Hello \n")
    value=f.write("world")
    print(value)
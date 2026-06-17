#list comprehension
# fruits=["apple","banana","orange","grapes","pine"]
# new_list=[]
# for x in fruits:
#     if "a" in x:
#         new_list.append(x)
# print(new_list)

##### a vako jati sabiiie aauxa

# using list comprehension #############################################
# fruits=["apple","banana","orange","grapes","pine"]
# new_list=[x for x in fruits if "a" in x]
# print(new_list)

#second method####################################################################
# number=[1,2,3,4,5,6]
# new_list=[]
# for num in number:
#     if num%2==0:
#         new_list.append("even")
#     else:
#         new_list.append("odd")
# print(new_list)

# #list comprehension
# new_list=["even",]



#third comprehension
# number=[1,2,3,4,5]
# new_list=[]
# for x in number:
#     new_list.append(x**2)
# print(new_list)

 # list comprehensionxxxxxxxxxxxxxxxxxxxxx
# number=[1,2,3,4,5]
# new_list=[x**2 for x in number]
# print(new_list)


#Tuple###########################################################
#creating tuple
# list=[]
# print(type(list))
###########################
# tuple=("ram",)
# print(type(tuple))
# ##########
# tup=(1,2)
# num1,num2,*num3=tup
# print(num1)
# print(num2)
# print(num3)
# # ######################
# tup=(1,2,3)
# num1,num2,*num3=tup
# print(num1)
# print(num2)
# print(num3)

##################
# tup=(1,2,3,4,5)
# num1,*num2,num3=tup
# print(num1)
# print(num2)
# print(num3)
###################
# tup=(1,2,3,4,5)
# *num1,num2,num3=tup
# print(num1)
# print(num2)
# print(num3)

# #Set class ################################
# set1={1,2,1,1,1,1,3,9,4,2}
# print(set1)


# ###################
# set1={"A","B","c","B"} #No order maintain
# print(set1)

#Access method:
# set1={"A","B","c","B"}
# for i in set1:
#     print(i)
# print(set1)

## Add######################################### 
# set1={"A","B","c","B"}
# set1.add("D")
# print(set1)
#remove ####################################

# set1={"A","B","c"}
# # set1.remove("z")### Error 
# set1.discard("z")
# set1.clear()### set empty
# del set1 # delete entire variable
# print(set1)









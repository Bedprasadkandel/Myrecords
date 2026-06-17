#Immutable data type
# s="Hello"
# s[0]="h"#  this will rise a type error:

# s="Hello"
# s="h" + s[1:]
# print(s)
 
# s="Hello"
# s="h" + s[1:]+ " " "world"
# print(s)

# s="Hello world"
# print(s.lower())

# s="  Hello Nepal    "
# print(s.lstrip())

# s="  Hello Nepal    "
# print(s.rstrip())

# s="##########@#######HELLOWORLD##########%#######"
# print(s.strip("#%@").lower().title().replace("HelloWorld", "Hello World"))

# s= "Hello-world-Nepal" 
# # print(s.split(","))
# print(s.split(","))



# s = "##########@#######HELLOWORLD##########%#######"
# print(s.strip("#%@").lower().title().replace("Helloworld", "Hello World"))


# #given_template="#####hello#world##########"
# # answer:HELLO WORLD count the lenth of before hello and after the world of #

# s="#####hello#world##########"
# answer=(s.strip("#").upper().split("#"))
# result=" ".join(answer)
# print(result)
# print("Before hello # count:",len(s)-len(s.lstrip("#")))
# print("After world # count:",len(s)-len(s.rstrip("#")))

s="  Hello world "
print(s.lower())
print(s.upper())
print(s.title())
print(s.split())
print(s.rstrip())
print(s.lstrip())
print(s.strip())
print(s.replace(" world"," " "Nepal"))


  
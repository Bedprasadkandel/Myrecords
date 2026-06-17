#module#####################
def greeting(name):
    print("Hello," + name)

def sum(a,b):
    result=a+b
    print("result",result)
    return result

def diff(a,b):
    result=a-b
    print("result",result)
    return result

def mul(a,b):
    result=a*b
    print("result",result)
    return result

name="abc"
print("name:", name)


# print("name",__name__)#"my module"
# if__name__=="__main__":
#     print("this is from mymodule")
#     print("hello my module")
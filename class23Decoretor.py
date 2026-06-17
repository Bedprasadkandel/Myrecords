#with out paramenter function and without parameter decorator
# def decorator1(fun):# fun= say_hello
#     def wrapper():
#         print("Something before function runs")
#         fun()
#         print("Something after the function runs")
#     return wrapper
# @decorator1  
# def say_hello():
#     print("hello")
# say_hello()

# #with  paramenter function and without parameter decorator
def decorator1(fun):# fun= say_hello 3
    def wrapper(*args,**kwargs):#4
        print("Something before function runs")#5
        fun(*args,**kwargs)#69
        print("Something after the function runs")#10
    return wrapper #3
@decorator1  #2 
def say_hello(x,y,**kwargs):#7
    print("hello",x,y)#8
say_hello("abc","der", name ="ram") #1 11


########################################
#with  paramenter function and with parameter decorator
# def greaterdecorator(value):
#     def decorator1(fun):# fun= say_hello
#         def wrapper(*args,**kwargs):
#             print("my name is :",value)
#             print("Something before function runs")
#             fun(*args,**kwargs)
#             print("Something after the function runs")
#         return wrapper
#     return decorator1
# @greaterdecorator("ram") 
# def say_hello(x,y):
#     print("hello",x,y)
# say_hello("abc","der")

######################################
#usecale of decorator
import time
def execution_time (func):# fun= say_hello
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Execution time of {end_time-start_time:.4f} seconds")
        return result
    return wrapper
@execution_time
def example_function(n):
    total=0
    for i in range(n):
        total= total+i
    return total
value= example_function(1000000)    


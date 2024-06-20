# types of variable

# 1. Instance Variable

# x= 5
# print(type(x));

# robi = 30 
# print(type(robi))

# name = "Rabi"
# print(type(name))

# s = str(20)
# print(type(s))

# i = int(30)
# print(type(i))

# f = float(30)
# print(type(f))


# age = [30,.21,45]
# rabi, sami, jami = age
# print(rabi)



# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# global variable

# name = "Rabi"
# def myfunc():
#     print("My name is " + name) 

# myfunc()

# name = "Projit"
# def function():
#     name = "Latif"
#     print ("my name is " + name)
# function()

# print("My name is " + name)



# def my_function():
#     local_variable = 10
#     print(f"The value of the local variable is {local_variable}")

# my_function()

# def my_function():
#     local_variable = "I am a local variable"
#     print({local_variable})

# my_function()

# x = "awesome"

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)




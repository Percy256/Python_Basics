#Group blocks of code
#There is need for code that is clean, reusable, maintainable
#def function_name():

# def afternoon():
#     print("Class starts at 2pm")
#     print("Attendees are close to 100")

#     #Calling a function
# afternoon()

#Arguments and Parameters
#Arguments
#Parameters
# def afternoon(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Attendees are close to 100")
# #Calling a function with parameters
# afternoon("Trevour", "Ssemaganda")

#Functions that perform a task (print) and functions that return a value(return)


# def phone_price(name, price):
#     return f"{name} and the price is {price}"

# print(phone_price("Samsung", 500000))

#Modules
#A simple calc
# def add(s, w):
#     return(s + w)
# def product(s, w):
#     return(s * w)

#     import module
#     print(module.product(8, 4))

    #importimg square root and factorial from the module math
# from math import sqrt, factorial#/ from math import *

# print(sqrt(100))
# print(factorial(10))

#Output
#Input and output in python
#input("prompt")

#Example of Input
# name= input("Enter your name: ")
# print("My name is, " + name)
    
#Example 2
number= int(input("Enter a value: "))
product= number * 10
print(product)

#Multiple inputs in python
# s, r, w= map(int, input("Enter the Values: ").split())
# print("The values are: ", end= "")
# print(s, r, w)

#How to capture input from a tuple
# w= (2, 4, 6, 5, 8)
# print("Current tuple")
# print(w)

# E= list(w)
# E.append(int(input("Enter new value: ")))
# w= tuple(E)
# print("Updates tuple: ")
# print(w)

# mylist= list(map(int, input("Enter the list values: ").spli()))
# myset= set(map(int, input("Enter the set values: ").split()))

# print(mylist)
# print(myset)
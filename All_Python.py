# #Python can be used on a server to create web applications
# print("Hello, World")

# """
# Web Development, Software development, Mathematics and system scripting
# """

# x= "5.0"
# print(type(x))

# #Multiple variables assigned to multiple values 
# a, b, c= "Orange", "Apple", "Mangoes"
# print(a)
# print(b)
# print(c)

# #Unpacking a collection
# names= ["Trevour", "Ssemaganda", "Isaac"]
# x, y, z= names
# print(x)
# print(y)
# print(z)

# #Outputing multiple variables
# A= "How"
# B= "are"
# C= "you ?"
# print(A, B, C)

# #Concatenating astring to an int without casting
# X= 5
# Y= "Trevour"
# print(X, Y)

# #Global Variables
# #These are variables created outside a function
# #Example
# p= "nice"
# def myFunc():
#     print("I am " + p)
# myFunc()

# d= "peter"

# def func():
#     d= "John"
#     print(d)

# func()
# print(d)

#Global keyword
# def myfunc():
#       global x
# x = "fantastic"

# myfunc()

# print("Python is " + x)

#Random module
# import random

# #f= range(6)
# print(random.randrange(1, 6))

# x= "Hello, Trevour"

# for X in x:
#     print(X)

# print(len(x))
# print("Hello" not in x)

# #Slicing in strings
# print(x[2:8])

# #Negative indexing
# print(x[-5:-2])

#Remove Whitespace
# x= "    Hello, World   "
# print(x.strip())
# #Replace characters in strings
# print(x.replace("H", "J").strip())
# #Split string
# print(x.split(","))

# #Format string
# age= 22
# stmt="I am Ssemaganda Trevour and am {} years old"
# print(stmt.format(age))
# #With multiple number of arguments
# name= "Ssemaganda Trevour"
# quantity=5
# price= 2500
# txt= "I am {} and i bought {} at {} shillings only"
# print(txt.format(name, quantity, price))

#FileHandling
#Key function for working with files in python is fopen()
# import os
# f= open("trevor.txt", "r")
#print(f.read())
#f.close()
#Reading only parts of the file
# print(f.read(10))
# print(f.readline())
# print(f.readline())

#Reading a file by looping through it
# for line in f:
#     print(line)
#Writing to a file
# f= open("trevor.txt", "a")
# f.write("This text has just been added in afterwards.")
# f.close()

# f= open("trevor.txt", "r")
# print(f.read())

# F= open("myFile.txt", "x")
# F.write("This is a new text file here.")
# F= open("myFile.txt", "r")
# print(F.read())
# F= open("myFile.txt", "a")
# F.write("I have added this text right here")
# print(F.read())

#Deleting a file
# import os
# if os.path.exists("trevor.txt"):
#     os.remove("trevor.txt")
# else:
#     print("File doesnot exist")

#Classes and objects

# class myClass:
#     def __init__(self, name, age):
#         self.name= name 
#         self.age= age

# myclass= myClass("Trevour", 25)
# print(myclass.name)
# print(myclass.age)

#Returning it as a string
#     def __str__(self):
#         return f"{self.name} and {self.age}"
# myclass1= myClass("John", 30)
# print(myclass1)

#Functions that carry out tasks

#     def myFunc(self):
#         print(f"I am {self.name} and am {self.age} years old.")

# myclass2= myClass("Trevour", 30)
# myclass2.myFunc() 

# class Employee:
#     raise_mt= 1.04

#     def __init__(self, first, last, pay):
#         self.first= first
#         self.last= last
#         self.email= first + last + "@gmail.com"
#         self.pay= pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
    
#     def apply_raise(self):
#         self.pay= int(self.pay * self.raise_amt)

# class Developer(Employee):
#     pass

# dev_1= Employee("Trevour", "Ssemaganda", 100000)
# dev_2= Employee("Phillip", "Bindya", 150000)

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)

# print(dev_1.fullname())
# print(dev_2.fullname())

#Inheritance
# class Person:
#     def __init__(self, fname, lname):
#         self.fname= fname
#         self.lname= lname

#     def printname(self):
#         print(f"{self.fname} {self.lname}")

# myPerson= Person("Trevour", "Ssemaganda")
# myPerson.printname()

# class Student(Person):
#     pass
# myPerson = Student("Isaac", "John")
# myPerson.printname()

#Give child class own __init__ method
# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.grad_year = year

#     def welcome(self):
#         print(f"Welcome {self.fname} {self.lname} to our {self.grad_year} graduation ceremony.")

# myPerson1= Person("Trevour", "Ssemaganda")
# myPerson= Student("Kizza", "Mark", 2018)
# myPerson1.printname()
# myPerson.printname()
# myPerson.welcome()

#Iterator
#This is an object that contains a countable number of values.
#An object that can be iterated over meaning you can traverse through all values.
#Consists of the methods __iter__() and __next__()

# #Example1
# mytuple= ("Milk", "Soda", "Water")
# myit= iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# #Strings as iterables
# txt= "banana"
# myite= iter(txt)
# print(next(myite))
# print(next(myite))
# print(next(myite))
# print(next(myite))
# print(next(myite))
# print(next(myite))

#Example2
# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
    
#     def __next__(self):
#         x= self.a
#         self.a+=1
#         return x
    
# myclass= myNumbers()
# myiter= iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#Example3:
# class myNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=20:
#             x= self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration

# myclass= myNumbers()
# myiter= iter(myclass)

# for x in myiter:
#     print(x)

#Polymorphism
# class Car:
#     def __init__(self, brand, model):
#         self.brand= brand
#         self.model= model

#     def move(self):
#         print(f"Drive!- {self.brand} and {self.model}")

# class Boat:
#     def __init__(self, brand, model):
#         self.brand= brand
#         self.model= model

#     def move(self):
#         print(f"Sail!- {self.brand} and {self.model}")

# class Plane:
#     def __init__(self, brand, model):
#         self.brand= brand
#         self.model= model

#     def move(self):
#         print(f"Fly!- {self.brand} and {self.model}")

# myCar= Car("Mercedes", "BMW")
# myCar.move()
# myBoat= Boat("Ship", "AEW")
# myBoat.move()
# myPlane= Plane("Airbus", "Boeing")
# myPlane.move()

#Generators
#Yield Keyword and Iterators are two terms involved when we discuss generators.
#A generator function is defined like a normal function but whenever it needs to generate
#a value, it does so with the yield keyword rather than the return keyword

# #Example1:
# def myGen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5

# #Driver code to check above generator function
# for value in myGen():
#     print(value)

# #Generator-object:
# #Generator function returns a generator object.
# #Generator objects are used either by calling the next method on the generator object or using the 
# #generator object in a "for in" loop.

# #Example2:
# def myGen():
#     yield 1
#     yield 2
#     yield 3
    
# #x is the generator object
# x= myGen()

# #Iterating over the generator object using next method
# print(next(x))  
# print(next(x))
# print(next(x))

#Context Managers:
from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f= open(file, mode)
    yield f
    f.close()

with open_file("myfile.txt", "w") as f:
    f.write("We are here to stay.")

print(f.closed)


    








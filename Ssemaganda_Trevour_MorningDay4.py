#Object-Oriented Programming(OOP)
#Key Concepts
#1. Class
#2. Encapsulation
#3.Inheritance
#4. Polymorphism
#5. Abstraction

"""
Class
"""
#Example1: Car

# class Car:
#     def _init_ (self, make, model, year):
#         self.make= make
#         self.model= model
#         self.year= year

#     def start_engine(self):
#         print("Engine started")

#     def stop_engine(self):
#         print("Engine stopped")

#     my_car= Car("Toyota", "Corolla", 2022)

# print(my_car.make)
# print(my_car.model)
# print(my_car.year)
# my_car.start_engine()
# my_car.stop_engine()

#Example3: Rectangle

# class Rectangle:
#     def _init_(self, length, width):
#         self.length= length
#         self. width= width

#     def calculate_area(self):
#         return self.length * self.width
    
#     def calculate_perimeter(self):
#         return 2 * (self.lenth + self.width)
    
#     #Create a rectangle
# my_rectangle= Rectangle(15, 5)
# print(my_rectangle.length)
# print(my_rectangle.width)

    #Calculate and display the area and perimeter
# print(my_rectangle.calculate_area())
# print(my_rectangle.perimeter())

    #Example4:University students
# class Student:
#     def __init__(self, name, year, course):
#         self.name= name
#         self.year= year
#         self.course= course
        
#     def display_details(self):
#         print("Name: ", self.name)
#         print("Year: ", self.year)
#         print("Course: ", self.course)

# #Create a student object
# my_student= Student("Jeff Geoff", 3, "Software Engineering")

# #Display the student details
# my_student.display_details()

#Object

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age= age

#     def greet(self):
#         print("Hello, my name is", self.name)
#         print("I am", self.age, "years old")

# #Create a Person object
# my_person1= Person("Jeff Geoff", 35)
# my_person2= Person("Trevor", 25)

#Access the person object attributes
# print(my_person1.name)
# print(my_person1.age)
# print(my_person2.name)
# print(my_person2.age)

# #Invoke our object method
# my_person1.greet()
# my_person2.greet()

#Exercise 1
#Calculate the area and circumference of a circle

#Circle

# class Circle:
#     def __init__(self, radius):
#             self.radius= radius

#     def calculate_area(self):
#             return 3.14 * self.radius * self.radius
    
#     def calculate_circumference(self):
#             return 2 * 3.14 * self.radius
    
#     #Create a Circle object
# my_circle= Circle(5)
# print(my_circle.radius)

#Calculate and display area and circle
# print(my_circle.calculate_area())
# print(my_circle.calculate_circumference())

#Exercise 1
#Calculate and dislay employee bonuses(o.5) of salary(employee1: 150000, employee2: 2300000)

# class Employee:
#     def __init__(self, name, salary):
#         self.name= name
#         self.salary= salary

#     def calculate_bonus(self):
#         #return 0.15 * self.salary
#         print(f"{self.name}  - {self.salary}")
    
# my_bonus= Employee("Trevor", 150000)
# my_bonus2= Employee("Amos", 230000)

# my_bonus.calculate_bonus()
# my_bonus2.calculate_bonus()

#Encapsulation
# Key main goal of encapsulations are

"""
1. To hide the implementation details of an object
2. To protect the object from changes
3. To protect the object from external changes
4. Code organization and modularity
"""

#Example: with a bank account
# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number= account_number #Encapsulates the ccount number attribute
#         self._balance= balance#Encapsulates the balance attribute

#     def deposit(self, amount):
#         self._balance += amount #Encapsulates the deposit
    
#     def withdraw(self, amount):
#         if self._balance >= amount:
#             self._balance -= amount
#         else: 
#             print("Insufficient funds")

#         def get_balance(self):
#             return self._balance
        
# #Create a Bank object
# my_account= BankAccount("123456789", 1000)

#Access the bank object and modify encapsulated attributes indirectly
# print(my_account._account_number)
# print(my_account._balance)
# my_account.deposit(500)
# print(my_account._balance)
# my_account.withdraw(2000)
# print(my_account._balance)

#Exercise 2: Convert temperature(37 celcius) from Celcius to Fahrenheit

# class Temp:
#     def __init__ (self, celsius):
#         self._celsius= celsius

#     def convert(self):
#         return (self._celsius * 1.8) + 32
    
# temp= Temp(37)
# temp._celsius=100
# print(temp.convert())


#Assignment1: Show encapsulation with employee information to give a 
#pay incrementation (Salary with employee information to new_salary)e.g from 850000 to 1000000

# class Employee_info:
#         def __init__ (self, salary):
#             self.salary= salary

#         def increment(self, salary):
#             print (self.salary * 0.15) + self.salary
    
# myEmployee_info= Employee_info()
# myEmployee_info.increment(850000)

class Employee_info:
    def __init__ (self, name, title,  salary):
        self._name= name
        self._title= title
        self._salary= salary

    def get_name(self):
        return self._name
    
    def get_title(self):
        return self._title
    
    def get_salary(self):
        return self._salary
    
    def set_salary(self, new_salary):
        self._salary= new_salary

    def increment(self, salary):
        self._salary += incrementAmount

#creating class object
myEmployee_info= Employee_info("Ssemaganda Trevour","Full Stack Developer",  850000)

#Accessing the name and salary
print("Employee Name: ", myEmployee_info.get_name())
print("Title: ", myEmployee_info.get_title())
print("Employee current salary: ", myEmployee_info.get_salary())

#Getting increment amount
incrementAmount= 150000
myEmployee_info.increment(incrementAmount)

#Printing new salary
print("New salary: ", myEmployee_info.get_salary() )





            







        
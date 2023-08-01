#Python Exception Handling
#Two types of errors i.e Syntaxt Errors and Exceptions
#Errors are problems in a program  due to which a program will stop execution while 
#Exceptions are raised when some internal events occur which change the normal flow of the program.
#Examples of exceptions include Syntaxt Error, TypeError, NameError, IndexError, KeyError, ValueError, AttributeError, IOError
#IOError, ZeroDivisionError, ImportError

# Example1
#SyntaxError
#Initialised age to 20
# age = 20
#Checking for elligibility
# if (age>30) This gives a syntax error due to the missing ":" and this will stop program from executing
#     print("You are past the age limit.") 

#Exceptions
#Example2
# X= 90
# Y= X/0 #Here the code is syntactically correct but ZeroDivisionError is raised which changes the normal 
# print(Y)#flow of the program but doesn't stop the program from execution
# print("We execute afterwards")

#Example3
# a= "Trevour"
# b= 40
# c= a + b
# print(c)#This will raise a TypeError since we are concatenating a string and an int witout any conversions made

#Handling Exceptions
#Here we are going to handle the previous exceptions we have encountered
#We use the "try" and "catch" statements to handle exceptions
#Statements that raise exceptions are kept inside the try clause and those that handle exceptions are kept inside the except clause

# Example4
# a= "Trevour"
# b= 40
# try:
#     c= a + b
# except TypeError:
#     print("We can't concatenate a string to an int without any conversions or casting")

# #Example5
# X= 90
# try:
#     Y= X/0 
# except:
#     print("DivisionByZero Error Raised")
# print("We execute afterwards")#This code will execute to the last code statement hence normal flow won't be disrupted

#Example6
# p= ["Trevour", "Ssemaganda", "Isaac"]

# try:
#     print(f"First element = " + p[0])
#     print("Fourth element = %d" %(p[3]))#This will cause the except clause to execute since index 3 is out od bounds in p
# except:
#     print("IndexOutOfBoundError Occured")

#Example6
# def fun(x):
#     if x < 4:
#         y= x/(x-3)
#         print("Value of y= ", y)
# try:
#     #fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("DivisionByZeroError occured.")
# except NameError:
#     print("Name Error Occurred.")

#finally clause
#This always carries the code that should always execute 

# try:
#     a= (int(input("Enter the first number: ")))
#     b= (int(input("Enter the second number: ")))
#     c= a/b
#     print("a/b= %d"%c)
# except:
#     print(c)
#     print("Can't divide by zero")
# finally:
#     print("This always executes.")

#raise clause
#This is used to force an exception to occur

# def divide_numbers(a, b):
#     try:
#         if b == 0:
#             raise ZeroDivisionError("Error: Division by zero")
#         result = a / b
#         return result
#     except ZeroDivisionError as e:
#         print("Error:", str(e))

# # Example usage
# num1 = 10
# num2 = 0

# result = divide_numbers(num1, num2)
# if result is not None:
#     print("Result:", result)

#File Handling
#A file contains a collection of data and information.
#Two types of files ie text file for characters and strings and binary file which stores data inform of bytes.
#File handling in python performs functions such as creating, reading, updating and deleting files.
#open()- Takes in two parameters i.e filename and mode
# syntax: f= open("file.txt", mode)
"""
"r"- Read, default value. Opens file for reading, error if the file does not exist.
"a"- Append, Opens a file for appending, creaates a file if it does not exist.
"w"- Write, opens a file for writing, creates a file if it doesn't exist
"x"- Create, Creates the specified file, returns an error if the file exists
"t"- Text, Default value, text mode
"b"- Binary, Binary mode e.g images
"""
#Example1


import os

def create_file(filename):
	try:
		with open(filename, 'w') as f:
			f.write('Hello, trevour!\n')
		print("File " + filename + " created successfully.")
	except IOError:
		print("Error: could not create file " + filename)

def read_file(filename):
	try:
		with open(filename, 'r') as f:
			contents = f.read()
			print(contents)
	except IOError:
		print("Error: could not read file " + filename)

def append_file(filename, text):
	try:
		with open(filename, 'a') as f:
			f.write(text)
		print("Text appended to file " + filename + " successfully.")
	except IOError:
		print("Error: could not append to file " + filename)

def rename_file(filename, new_filename):
	try:
		os.rename(filename, new_filename)
		print("File " + filename + " renamed to " + new_filename + " successfully.")
	except IOError:
		print("Error: could not rename file " + filename)

def delete_file(filename):
	try:
		os.remove(filename)
		print("File " + filename + " deleted successfully.")
	except IOError:
		print("Error: could not delete file " + filename)


if __name__ == '__main__':
	filename = "trevor.txt"
	new_filename = "new_trevor.txt"

	create_file(filename)
	read_file(filename)
	append_file(filename, "This is some additional text.\n")
	read_file(filename)
	rename_file(filename, new_filename)
	read_file(new_filename)
	#delete_file(new_filename)









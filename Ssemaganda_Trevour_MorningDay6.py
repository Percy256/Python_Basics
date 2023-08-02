#Day 06
#Advanced topics in python

"""
-Regular Expressions
-Generators and iterators
-Decorators
-Context managers
-Multithreading and multiprocessing
"""
#Regular Expressions
#Regular expressions (regex) are a form of pattern matching that is used to search for patterns in strings.
#Regular expressions can be used to search for patterns in strings.
"""_summary_
\d: Matches any digit (0-9).
\w: Matches any alphanumeric character (a-z, A-Z, 0-9 and underscore).
\s: Matches any whitespace character (space, tab, newline).
.: Matches any character except a new line.
*: Matches zero or more occurences of the preceding chracter or group.
+: Matches one or more occurences of the preceding character

"""

#Matching and Searching
#regex re.match(), re.search(), re.findall()

#Example1 Demostrating regex | Match First Word, Match Group word, Match All Numbers
# import re
# text = "Hello, my name is Trevor. I am a student at MUK"
# #Match First Word
# match= re.search(r"\b\w+\b", text)

# if match:
#     print("Match: ", match.group())

# matches= re.search(r"\d+", text)
# print("Matches: ", matches)

#Example2 validate email format or email address
# import re
# def validate_email(email):
#     pattern= r'^[\w\.-]+@[\w\.\-]+\.\w+$'
#     if re.match(pattern, email):
#         return True
    
#     else: 
#         return False
    
#     #Example usage
#     email1= "trevoursemaganda@gmail.com"
#     email2= "trevoursemaganda@gmailcom"

#     print(validate_email(email))
#     print(validate_email(email2))

#Generators and iterators
# 'yield' generator
# Iterator '__iter__' "__next__" iterator

# def factorial(n):
#     #Return the factorial of a number
#     if n==0:
#         yield 1
#     else:
#         yield n*factorial(n-1)
    
#     #print the factorial of a number from 1 - 10
#     for i in range(1, 10):
#         print(factorial(i))


# def squares():
#     for i in range(1, 10):
#         yield i**2

#Create an iterator object that yields the square of numbers from 1 - 10

# squares_iterator= squares()

# #Print the first 5 squares of numbers from 1 to 10
# for i in range(5):
#     print(next(squares_iterator))

#Decorators @my_decorator
#Decorators in Python allows you to modify the behavior of functions or clsses without directly changing their source code. This

# def my_decorator(func):
#     def inner():
#         print("This is the decorator")
#         func()
#     return inner
    
#     @my_decorator
#     def outer_decorator():
#         print("This is outer decorator ")

    # outer_decorator()
# Decorators
# '@decorator_name' is the name of the decorator

# #Example2:
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         #Code to be executed before the original function
#         print("This is my decorator before function execution.")
#         result= func(*args, **kwargs)
#         #Code to be executed after the original function
#         print("This is my decorator after function execution.")
#         return result
#     return wrapper

# @my_decorator

# def my_function():
#     print("Inside the function")
# my_function()

#Example3:
# def my_decorator(cls):
#     class ModifiedClass:
#         def __init__(self, *args, **kwargs):
#             self.instance = cls(*args, **kwargs)

#         def my_method(self):
#             print("Modified method")

#     return ModifiedClass

# @my_decorator
# class MyClass:
#     def my_method(self):
#         print("My Original method")

# my_instance= MyClass()
# my_instance.my_method()

# #Context Manager 
# #An object that defines a temporary context for a block of code
# #Example1: Demonstrate a context manager to open a file and return a context manager instance

# def open_file(filename):
# #Open a file and return a context manager instance
#     file= open(filename, "r")

#     def __enter__():
#         return file
    
#     def __exit__(self, exc_type, exc_value, exc_tb):
#         file.close()

#         return __enter__, __exit__
    
# with open_file("my_file.txt") as f:
#     contents= f.read()

#Exacmple2: Demonstrate a context manager using a time series

# import time

# class Timer:
#     def __enter__(self):
#         self.start_time= time.time()
        
#     def __exit__(self, exc_type, exc_value, traceback):
#         end_time= time.time()
#         execution_time= end_time - self.start_time
#         print(f"The time for this execution {execution_time} seconds elapsed")

# #With Example usage
# with Timer():
#     #Measure the execution time
#     time.sleep(2)

#Assignment A7:
#Show a context manager for file handling that automatically opens and closes a file.

class Open_File():

    def __init__(self, filename, mode):
        self.filename= filename
        self.mode= mode

    def __enter__(self):
        self.file= open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with Open_File("mytxt.txt", "w") as f:
        f.write("Hey, am Ssemaganda Trevour and this is my sample text.")

print(f.closed)

#b) Shows a context manager for managing a database connection.

import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connection(path):
     conn= sqlite3.connect(path)
     cursor= conn.cursor()
     yield cursor
     conn.commit()
     conn.close()


with db_connection("mydb.db") as c:
    c.execute("CREATE TABLE IF NOT EXISTS person ("
             "name VARCHAR(255),"
              "age INT);")
    

#Multithreading and Multiprocesing
"""
    Techniques that can be used to improve the performance of a python program
    """
    #Multithreading- Is a technique where multiple threads are created within a single process
    #Multiprocessing- Is a technique where multiple processes are created
#Example of multithreading
# import threading

# def task(name):
#      print(f"Running task {name}")

# #Create multiple threads
# threads= []
# for i in range(10):
#      t= threading.Thread(target=task, args=(f"Thread {i}",) )
#      threads.append(t)
#      t.start()

#      #Wait for all threads to finish 

#      for t in threads:
#             t.join()

#Example of multiprocessing

# import multiprocessing
# def process_task(name):
#     print(f"Processing task {name}")

# #Create a pool of processes
# pool= multiprocessing.Pool(processes=5)

# #Submit multiple task to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=(f"Process {i}",))

# #Close the pool and wait for all processes to finish
# pool.close()
# pool.join()

#Example: Demonstrate use of multithreading and multiprocessing
# import threading
# import multiprocessing

# def task(name):
#     print(f"Running task {name} on thread {threading.current_thread().name} with process {multiprocessing.current_process().name}")

# #Create multiple threads to run
# threads=[]
# for i in range[4]:
#     t= threading.Thread(target= task, args=(f"Thread {i}",))
#     threads.append(t)
#     t.start()

# #Wait for all threads to finish
# for t in threads:
#     t.join()
#Assignment7:
#Show a multithreading and multiprocessing  that allows us to run the function for different amounts of time.
import time
import threading
from multiprocessing import Process


def run_function(duration):
    print(f"Function started for {duration} seconds")
    time.sleep(duration)
    print(f"Function finished for {duration} seconds")


def run_multithreading():
    durations = [1, 2, 3]  

    
    threads = []
    for duration in durations:
        t = threading.Thread(target=run_function, args=(duration,))
        threads.append(t)
        t.start()

    
    for t in threads:
        t.join()

    print("Multithreading finished")


def run_multiprocessing():
    durations = [1, 2, 3]  

    
    processes = []
    for duration in durations:
        p = Process(target=run_function, args=(duration,))
        processes.append(p)
        p.start()

    
    for p in processes:
        p.join()

    print("Multiprocessing finished")


run_multithreading()
run_multiprocessing()
    



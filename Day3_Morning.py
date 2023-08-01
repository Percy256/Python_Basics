#Day3
#Basic Operators and Expressions(Input and Output operators)

"""
    -Arithmetic Operators
    + Addition
    - Subtraction
    * Multiplication
    / Division
    % Modulus
    ** Exponential

    -Comparison Operators
    ==Equal to
    != Not Equal !==
    >Greater than
    <Less than
    >= Greater than or equal to
    <= Less than or equal to

    -Logical Operators
    Logical AND 'and'
    Logical OR: 'or'
    Logical NOT: 'not

    -Assignment Operators
    Assign value: '='
    Add value: '+'
    Add and assign a value: '+='
    Subtract and assign value: '-='
    Multipl and assign value: '*/'
    Divide and assign value: '/*'
    Modulus and assign: '%='
    Exponential and assign: '**='

    -Membership Operators:
    In: 'in' operator checks if a value exists in a sequence
    Not in: 'not in': Checks if a value doesnot exist in a sequence

    -Identity Operators:
    Is: 'is' operator that checks if two values are the same 
    Is not: 'is not' operator checks if two values are not the same

    """

#Examples of arithmetic operators
#Addition
x= 50 + 45
print(x)
#Subtraction
y= 50 - 45
print(y)
#Multiplication
z= 50 * 45
print(z)
#Division
a= 50 / 45
print(a)
#Modulus
b= 10 % 3
print(b)
#Exponential
c= 2**4
print(c)
#Divide
d= 50 // 45
print(d)

#eXAMPLES OF cOMPARISON OPERATORS
A= 20
B=10
#greater than 
if(A>B):
    print("A is greater than B")
    print(A>B)
#Less than 
if a<b:
    print("A is less tha B")
    print(A<B)

#Greater than or eual to
if A>=B:
    print("A is greater than or equal to B")
    print(A>=B)
#Less than or equal to
if A<=B:
    print("A is less than or equal to B")
    print(A<=B)
#Equal to
if A==B or A>B:
    print("A is equal to B")
    print(A==B)
#Not equal to 
if A != B:
    print("A is not equal to B")
    print(a !=b)
#less than or equal to
print(A<=B)

#Examples with Logicsl operators
#Logical Operators
a= True
b= False

#Logical And
print(a and b)

#Logical OR
print(a or b)

#Logical NOT
print(not a)
print(not b)

#Bitwise XOR operations
result_not= ~a


#Example and Assignment
#Create a simple calculator function to calculate (add, subtract, multiply, divide)
def add(a, b):
    return a + B

def subtract(a, b):
    return a - B

def multiplication(a, b):
    return a * B

def divide(a, b):
    return a/b

def main():
    print('Jeff Simple Calculator')
    number1= float(input("Enter the first number: "))
    number2= float(input("Enter the second number: "))
    operator= input("Enter the operator '+, -, /, *")

    if operator== '+':
        result= add(number1, number2)
    elif operator == '-':
        result= subtract(number1, number2)
    elif operator == '*':
        result= multiplication(number1, number2)
    elif operator == '/':
        result= divide(number1, number2)
    else:
        print('Invalid Operator')
        return
    print("The result is", result)



    if ___name___ == '___main___':
        main()

        #tkinter learn
        #Assignment:1 create a simple calculator program with a GUI interface. Make the title of the calculator program window with your name e.g "Jeff Geoff Simple calculatorld "




    print("Addition: ", add(a, b))
    print("Subtraction: ", subtract(a, b))
    print("Multiplication: ", multiplication(a, b))
    print("Division: ", divide(a, b))



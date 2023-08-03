class Employee:
    def __init__(self, name, title, salary):
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

myEmployee= Employee("Rashid Kisejjere", "Programmer", 2850000)

print("Employee Name: ", myEmployee.get_name())
print("Employee Title: ", myEmployee.get_title())
print("Employee Salary: ", myEmployee. get_salary())

incrementAmount= 1150000
myEmployee.increment(incrementAmount)

print("New Salary: ", myEmployee.get_salary())
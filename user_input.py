name= input("What is your name?: ")
age= int(input("How old are you?"))
age += 1

print("Hello " + name)
print("You are " + str(age) + " years of age dear.")
salute= "Am " + name + " and i am {}"
print(salute.format(age))

print(f"I an {age} years of age")

years={
    2001: "I am 22 years old",
    2002: "I am 21 years old",
    2003: "I am 20 years old",
    2004: "I am 19 years old",
    2005: "I am 18 years old",
    2006: "I am 17 years old",
    2007: "I am 16 years old",
}

ques=int(input("Which year were u born?"))
if ques in years:
    print(years[ques])
else:
    print("Your not elligible for this program:")
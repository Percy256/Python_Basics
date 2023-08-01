#Exercise1:
#1
names=["Phillip", "Rashid", "Trevour", "Marble", "Cathy"]
print(names[1])

#2
names[1]= "Devote"
print(names)

#3
names.append("Elmer")
print(names)

#4
names.insert(2, "Bathel")
print(names)

#5
names.pop(3)
print(names)

#6
print(names[-1])

#7
cars=["Volvo", "Tesla", "BMW", "Forester", "GWagon", "Sienta", "Raum"]
print(cars[2:5])

#8
countries=["Uganda", "America", "Argentina", "Kenya", "Brazil", "Kenya"]

copyCountries= countries.copy()
print(copyCountries)

#9
for country in countries:
    print(country)

#10
animals=["Lion", "Leopard", "Cows", "Cats", "Elephant"]
animals.sort()
print(animals)

animals.sort(reverse= True)
print(animals)

#11
for animal in animals:
    index = animal.find("a")
    if(index != -1):
        print(animal)


#12
first_name= ["Ssemaganda", "Trevour"]
second_names=["Isaac", "Percy"]

All_names= first_name + second_names
print(All_names)

#Exercise2:
#1
x= ("Samsung", "iphone", "tecno", "redmi")
print(x[0])

#2
print(x[-2])

#3
xlist= list(x)
xlist[1]= "itel"
xlist= tuple(xlist)
print(xlist)

#4
ylist= list(x)
ylist.append("Huawei")
ylist= tuple(ylist)
print(ylist)

#5
for phones in x:
    print(phones)

#6
zlist= list(x)
zlist.remove(zlist[0])
zlist= tuple(zlist)
print(zlist)

#7
myCities=tuple(("Kampala", "Nairobi", "Kigali", "Dodoma", "Bujumbula"))
print(myCities)

#8
(Uganda, Kenya, Rwanda, Tanzania, Burundi)= myCities
print(Uganda)
print(Kenya)
print(Rwanda)

#9
print(myCities[1:4])

#10
fnames=("Ssemaganda", "Trevour")
lnames=("Isaac", "Percy")

bnames= fnames + lnames
print(bnames)

#11
colors=("Red", "Green", "Brown", "Black", "White")
Colors= colors * 3
print(Colors)




#12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# counter= 0
# for item in thistuple:
#     if item==8:
#          counter+=1
#          print(counter)
print(str(thistuple.count(8)) + " times")



#Exercise3:
#1
favorite_beverages=set({"Soda", "Juice", "Wine"})
print(favorite_beverages)

#2
favorite_beverages.add("Beers")
favorite_beverages.add("LemonJuice")
print(favorite_beverages)

#3
mySet={"oven", "kettle", "microwave", "refrigerator"}
print("microwave" in mySet)

#4
mySet.remove("kettle")
print(mySet)

#5
for one in mySet:
    print(one)

#6
people={"John", "Ivan", "Peter", "Trevour"}
two= ["Hey", "Hello"]

ztwo= set(two)
print(people.union(ztwo))

#7
ages={21}
myNames={"Ssemaganda", "Trevour"}
print(ages.union(myNames))

#Exercise4:

#1
x=22
y= "Trevour"
print(str(x) + y)

#2
txt="    Hello,     Uganda!    "

stripped= txt.strip()
print("Our stripped string is ", stripped)

#3
print(txt.upper())

#4
print(txt.replace("U", "V"))

#5
y= "I am proudly Ugandan"
print(y[1:5])

#6
x="All \"Data Scientists\" are cool"
print(x)

#Exercise5:
Shoes={
    "brand": "Nick",
    "color": "black",
    "size": 40,
}

print(Shoes["size"])

#2
Shoes["brand"]= "Adidas"
print(Shoes)

#3
Shoes["type"]= "Sneakers"
print(Shoes)

#4
print(Shoes.keys())

#5
print(Shoes.values())

#6
print("size" in Shoes)

#7
for qualities in Shoes:
    print(qualities)

#8
Shoes.pop("color")
print(Shoes)

#9
Shoes.clear()
print(Shoes)

#10
myDetails={
    "First Name": "ssemaganda",
    "Second Name": "Trevour",
    "Age": 22,
    "Address": "Kampala"
}

myDetails2= myDetails.copy()
print(myDetails2)

myfamily = {
  "1st" : {
    "name" : "Amos",
    "year" : 1997
  },
  "2nd" : {
    "name" : "Diana",
    "year" : 1995
  },
  "3rd" : {
    "name" : "Joan",
    "year" : 1997
  }
}

print(myfamily)









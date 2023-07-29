age = 36
txt = "My name is John, I am " + age
print(txt) 

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

name = "Bilal Khan" 
age = 13
city = "Wah Cantt" 
bioData = "Hi, its {}, I'm {} old and live in {}"
bio = bioData.format(name, age, city)

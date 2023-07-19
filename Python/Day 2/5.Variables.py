#Variables or Data Type
#The data stored in memory can be of many types. 
#For example, a person's age is stored as a numeric 
#value and his or her address is stored as alphanumeric 
#characters. Python has various standard data types that 
#are used to define the operations possible on them and 
#the storage method for each of them.
#Python has five standard data types −
#Numbers
#String
#List
#Tuple
#Dictionary

#!/usr/bin/python

counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter) 
print(miles) 
print(name)

# Multiple Assignment 
a = b = c = 1
a,b,c = 1,2,"john"

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(list)        # Prints complete list

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print(tuple)        # Prints the complete tuple 

dict['one'] = "This is one" 
print(dict['one'])     # Prints value for 'one' key

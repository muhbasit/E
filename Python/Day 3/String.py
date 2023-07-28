print('Hello')

# assign strimg to variable
a = "Hello"
print(a)

# multi-line string
b = """
Machine learning (ML) is an umbrella 
term for solving problems for which 
development of algorithms by human
programmers would be cost-prohibitive,
and instead the problems are solved by 
helping machines 'discover' their 'own' 
algorithms,[1] without needing to be 
explicitly told what to do by any
human-developed algorithms.
"""
print(b)

#Indexing strings 
c = "Hello, World!"
print(c[1])
print(c[1:])
print(c[1:4])
print(c[1:4:2])
print(c[1:-1])
print(c[:6])
print(c[:])
print(c[2:5])
print(c[-1:-5])

for i in b:
  print(i) 

print(len(a))
print(len(b))
print(len(c)) 

if "Machine" in b:
  print("Yes, is present.")

print(b.upper()) # Convert string to upper case
print(b.lower()) # Convert string to lower case 
print(b.strip()) # remove whitespace 
print(b.replace("M", "m")) #reolace M with m
print(b.split(",")) # split string with comma

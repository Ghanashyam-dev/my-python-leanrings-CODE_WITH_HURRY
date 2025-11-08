name = " ghanashyam jr hello "
# strings are immutable .

 
# name[0] = "r"  # here cannot change original string in memory.

# length of stering
a = len(name)
print(a)


# upper and lower 
print(name.upper())
print(name.lower())
print(name) # original string remaains same 
# capitalize ,only 1st letter 
print(name.capitalize()) 

# title , every starting letter after space is capitalized 
print(name.title())

# string , remove empty charecter and new lines 
print((name.strip()))
print((name.lstrip()))
print((name.rstrip()))

# find , gives inbdex of 1st occurance of  given letter 
print(name.find("jr"))

# replace , replace the given word 
print(name.replace("jr","kamal"))

# splite , splites the given string with a given charecter into a list 
text = "apple,banana,orange"
print(text.split(",")) 

print(text.join(["apple,banana,orange,mango"])) # list to string convertion 

text = "Python123"
print(text.isalpha()) # Output: False
print(text.isdigit()) # Output: False
print(text.isalnum()) # Output: True
print(text.isspace()) # Output: Fals

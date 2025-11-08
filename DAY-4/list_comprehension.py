# list contaning table of 5 

''''a = [ ]
print(type(a))
print(a)
t = 900000
for i in range(1,11):
    b = f"{t} x {i} = {i * t}" 
    a.append(b)

print(a)
'''
# list comprehension , makes it esay then above procces! .
a = [5*i for i in range(1,11)]
print(a)

b = [i**2 for i in range(5)]
print(b)

c = [i**2 for i in range(1,11)]
print(c)
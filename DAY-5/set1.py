a = {23,3,1}
b = {23,4,55,2,1}

# set oparation 

c = a.union(b)
print(c)

d = a.intersection(b)
e = b.intersection(a)
print(d,e)

f = a.difference(b)
g = b.difference(a)

print(f,g)
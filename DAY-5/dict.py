# these are key-value pairs 

d = {"harry" : 34 , 
     "jack":56,
     "age of harry":18,
     "age of jack":17}


print(type(d))
print(d)
print(d["harry"])
d["harry"] = 64
print(d)

d['gh'] = 54

print(d)

print(d.keys())
print(d.values())
print(d.items())
d.pop("harry")
print(d)

d_1 = {i: i*5 for i in range(1,11)}
print(d_1)



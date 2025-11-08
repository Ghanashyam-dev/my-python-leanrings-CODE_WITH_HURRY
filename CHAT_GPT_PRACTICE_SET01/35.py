d = {'name': 'ghana', 'age': 18}
d_1 = {}
for k,v in d.items():
    d_1[v] = k
    
    
print(d_1) 

dic_1 = {"name": "ghana", "age": 18}

for k, v in dic_1.copy().items():
    dic_1[v] = k
    del dic_1[k]

print(dic_1)


dic = {"a":12,"b":34,"c":4}
a = []
for key,value in dic.items():
    a.append(value)

a.sort()
high = a[len(a)-1]


for key,value in dic.items():
    if high == value:
        print(key)
    



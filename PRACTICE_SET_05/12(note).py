product_prise = {"A":1200,
                 "B":1300,
                 "C":7890,
                 "D":6540}



a = []
for key, value in product_prise.items():
    a.append(value)
a.sort()
h =  (a[len(a)-1])

for key, value in product_prise.items():
    if value == h :
        print(key)


# key = next((k for k, v in product_prise.items() if v == target))
# print(key)  

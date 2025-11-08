coordinates = (10, 20)
coordinates_1 = []

for i in range (len(coordinates)):
    coordinates_1.append(coordinates[i])

print(coordinates_1)
coordinates_1[0] = 50
print(coordinates_1)
print(coordinates)
coordinates = tuple(coordinates_1)

print(coordinates)


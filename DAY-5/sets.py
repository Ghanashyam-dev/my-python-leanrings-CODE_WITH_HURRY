# collection of well defined objects , elements cannot be repeated here .

set_1 = {1,23, 2, 11,6.8}
print(type(set_1))
print(set_1)
# print(set_1[1]) # no indexing as it is unordered

set_1.add(45)
set_1.add(4534)
print(set_1)

set_1.remove(2)
print(set_1)

set_1.discard(595959)  # if element not present it wont throw error unlike remove method.
print(set_1)
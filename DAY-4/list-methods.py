# list - mutable , ordered data
marks = [ 5, 2, 20, 99, 21, 5, 7]
marks_1 = [ 55, 66, 77]

print(marks)
# changes the original list , adds 63 at end of the list
marks.append(63)
print(marks)

# pop out the last item and return by defult
marks.pop()
print(marks)


# insert(at ehich index, what to be nserted their), the currect index is pushed to next index .
marks.insert(0,"hello")
print(marks)

# addes the another list_1 at last index of list
marks.extend(marks_1)
print(marks)

print(marks_1)

marks.remove("hello")

marks.sort()
print(marks)

marks.reverse()
print(marks)

#pop takes only index of item which should be deleted out.
a = marks_1.pop(2)
print(marks_1)
print(a)  # pop return the item which is deleted

print(marks)
print(marks_1)

# index takes the item and return the index of that item from the list
print(marks_1.index(66))


b = marks_1.copy()
print(b)



marks_1.clear()
print(marks_1)

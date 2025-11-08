name = input("Enter words: ")

name_2 = name[::-1]
if name == name_2:
    print("yes it is a palindrome")
else :
    print("No it is not a palindrom")
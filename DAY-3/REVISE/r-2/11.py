pass_word = "ghanashyamjr_09_"
a = (input("Enter pass: "))
while True:
    a = (input("Wrong pass! Reenter the pass:"))
    if a == pass_word:
        print("You are loged in!")
        break
    else:
        continue
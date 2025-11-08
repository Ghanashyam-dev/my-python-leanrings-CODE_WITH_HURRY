age = int(input("Enter age: "))

if age < 0 :
    print("Enter age more than 0 ")
elif age < 18 :
   print("You are not eligible to vote")
elif age >= 18 and age<100 :
    print("You are eliible to vote")
elif age > 100:
    print("you enter age more than 100")
else :
    print("Reenter the age!")
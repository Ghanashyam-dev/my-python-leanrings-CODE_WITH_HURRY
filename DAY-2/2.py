# match case  
#It simplifies complex conditional logic.

a = int(input("Enter a number between 1 to 5 :\n"))

match a :
    case 1 :
        print("you won a car ")
    case 2 :
        print("you won a bike")
    case 3 :
        print("you won a auto")
    case 4 :
        print("you won a DELL Laptop")
    case 5:
        print("opps, u won a toy")
    case _:
        print("input only numbers between 1 to 5 to win a price")

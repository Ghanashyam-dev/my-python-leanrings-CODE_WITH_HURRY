n = int(input("Enter a number: "))
if n > 7 or n <=0 :
    print("Enter a correct number between 1 to 7!")
match n :
    case 1 :
        print("Sunday")
    case 2 :
        print("Monday")
    case 3 :
        print("Tuesday")
    case 4 :
        print("Wednesday")
    case 5 :
        print("Thursday")
    case 6 :
        print("Friday")
    case 7 :
        print("Saturday")
n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))


print("choose oparation below\n1 - for add\n2 - for sub\n3 - for multiplication\n4 - for division")

o = int(input("Enter the oparation: "))

match o :
    case 1 :
        print(n1 + n2)
    case 2 :
        print(n1 - n2)
    case 3 :
        print(n1 * n2)
    case 4 :
        print(n1 / n2)
a = int(input("Enter a number 1 : "))
b = int(input("Enter a number 2 : "))
print("choose oparations below\n1 for addition\n2 for substraction\n3 for multiplication\n4 for division")
oparation = int(input("choose oparation: "))
if oparation == 0 or oparation < 1 or oparation > 4 :
    print( "please enter number from 1 to 4 to do the oparation!")
else :
    match oparation:
        case 1 :
            print(a + b)
        case 2 :
            print(a - b)
        case 3 :
            print(a * b)
        case 4 :
            print(a / b)









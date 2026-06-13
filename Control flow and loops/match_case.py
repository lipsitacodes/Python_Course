a = int(input("Enter the value between 1 to 10: "))
match a:
    case 1:
        print("You Won a Iphone.")
    case 3:
        print("The won a Macbook.")
    case 5:
        print("You won a Tesla.")   
    case _:
        print("Better Luck Next Time.")
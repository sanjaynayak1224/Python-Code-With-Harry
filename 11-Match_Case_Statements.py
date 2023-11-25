x=None
x=(input("enter a number: "))
x=int(x)
    
match int(x):
    case 0:
        print("Noob")
    case 1:
        print("not bad")
    case 2:
        print("pro")
    case _ if x==16:
        print("you need therapy")
    case _ if x==15:
        print("x value is 15")
    case _:
        print('invalid ')

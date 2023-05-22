while True:
    print("Please choose one of the following options: \n1-Nice Message\n2-Area of a rectangle\n3-Area of triangle\n4-Times Table\n5-Exit")
    opt = int(input())
    if opt == 1:
        print("You do not smell so bad today!")
    elif opt == 2:
        h = float(input("Enter Height: "))
        b = float(input("Enter the base: "))
        print(f"The area of this rectangle is {h*b} cm^2")
    elif opt == 3:
        h = float(input("Enter Height: "))
        b = float(input("Enter the base: "))
        print(f"The area of this triangle is {h*b*0.5} cm^2")
    elif opt == 4:
        n = int(input("Enter whole number: "))
        for i in range(1, 11):
            print(f"{n}x{i}={n*i}")
        print("That's all folks!")
    elif opt == 5:
        break
    else:
        print("Whoooooopsie! - no such option. Try again!")
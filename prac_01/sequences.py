x = int(input("Please enter the initial value x："))
y = int(input("Please enter the initial value y："))

while True:
    print("menu:")
    print("1. Displays even numbers from x to y")
    print("2. Displays odd numbers from x to y")
    print("3. Displays the square of a number from x to y")
    print("4. exit")

    choice = input("choose (1/2/3/4)：")

    if choice == "1":
        # Displays even numbers from x to y
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=" ")
    elif choice == "2":
        # Displays odd numbers from x to y
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end=" ")
    elif choice == "3":
        # Displays the square of a number from x to y
        for i in range(x, y + 1):
            print(i * i, end=" ")
    elif choice == "4":
        break
    else:
        print("Invalid")

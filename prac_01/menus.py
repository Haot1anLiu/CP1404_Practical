name = input("Enter name: ")

# Display the menu
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

# Get the user's choice
choice = input(">>> ").upper()

while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid ")

    # Display the menu again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    # Get the user's choice again
    choice = input(">>> ").upper()

    print("Finished.")

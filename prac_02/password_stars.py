def get_password(min_length):
    password = input("Please enter a password: ")
    while len(password) < min_length:
        print(f"Password should be at least {min_length} characters long.")
        password = input("Please enter a password: ")
    return password

def print_asterisks(password):
    print('*' * len(password))

def main():
    min_length = 8
    password = get_password(min_length)
    print_asterisks(password)

if __name__ == "__main__":
    main()
#Refactor password check program to use functions





import random
from score import determine_result


def get_valid_score():

    while True:
        try:
            score = float(input("Please enter a score (0-100 inclusive): "))
            if 0 <= score <= 100:
                return score
            else:
                print("The score must be between 0 and 100 inclusive.")
        except ValueError:
            print("Please enter a valid number.")


def print_stars(score):
    """Print stars equal to the score."""
    print('*' * int(score))


def main():
    score = get_valid_score()
    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Choose an option: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_result(score))
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Have a nice day!")
            break
        else:
            print("Invalid.")


if __name__ == "__main__":
    main()

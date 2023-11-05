
from guitar import Guitar

def main():
    guitars = []

    # Load existing guitars from the file
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name, year, cost = parts[0], int(parts[1]), float(parts[2])
            guitars.append(Guitar(name, year, cost))

    # Get new guitar information from the user
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")

    # Sort the guitars list by year
    guitars.sort()

    # Save the updated guitars list to the file
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            print(guitar)
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()

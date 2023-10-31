FILE_NAME = "test.csv"

def main():
    file_data = read_file(FILE_NAME)
    champion_countries, win_counts = process_data(file_data)
    display_data(champion_countries, win_counts)

def read_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header
        return [line.strip().split(",") for line in in_file]

def process_data(file_data):
    win_counts = {}
    champion_countries = set()
    for data in file_data:
        champion_countries.add(data[1])
        win_counts[data[2]] = win_counts.get(data[2], 0) + 1
    return champion_countries, win_counts

def display_data(champion_countries, win_counts):
    print("Wimbledon Champions:")
    for champion, count in win_counts.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(champion_countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(champion_countries)))

if __name__ == "__main__":
    main()
<<<<<<< HEAD
=======

>>>>>>> origin/master

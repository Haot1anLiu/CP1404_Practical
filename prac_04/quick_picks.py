import random

MIN_NUM = 1
MAX_NUM = 45
NUMS_PER_PICK = 6

def main():
    num_picks = int(input("How many quick picks? "))

    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print_formatted_pick(quick_pick)

def generate_quick_pick():
    pick = []
    while len(pick) < NUMS_PER_PICK:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in pick:
            pick.append(num)
    pick.sort()
    return pick

def print_formatted_pick(pick):
    for num in pick:
        print(f"{num:2}", end=' ')
    print()

if __name__ == "__main__":
    main()


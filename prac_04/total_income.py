def main():
    incomes = collect_incomes()
    print_report(incomes)


def collect_incomes():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    return incomes


def print_report(incomes):
    """Displays monthly income reports."""
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes, start=1):
        total += income
        print(f"Month {month} - Income: ${income:.2f}   Total: ${total:.2f}")


if __name__ == "__main__":
    main()

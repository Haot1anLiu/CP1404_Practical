from prac_07 import project

MENU = """Menu:
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def load_file(readable_file):
    """Loads inputted file"""
    my_projects = []
    with open(readable_file, 'r') as opened_file:
        opened_file.readline()  # Skip the header
        for line in opened_file:
            parts = line.strip().split('\t')
            my_projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    return my_projects


def save_to_file(writable_file, my_projects):
    """Saves to inputted file"""
    with open(writable_file, 'w') as opened_file:
        for project in my_projects:
            opened_file.write(project.__repr__() + '\n')


def display_projects(projects):
    """Displays inputted projects"""
    sorted_projects = sorted(projects)
    print("Incomplete projects:")
    for project in sorted_projects:
        if not project.is_completed():
            print(f"  {project}")
    print("Completed projects:")
    for project in sorted_projects:
        if project.is_completed():
            print(f"  {project}")


def display_filtered_projects(projects, date):
    """Displays inputted projects started after inputted date"""
    day, month, year = date.split("/")
    print(f"Show projects that start after date (dd/mm/yy): {date}")
    for project in sorted(projects, key=lambda x: (x.start_year, x.start_month, x.start_day)):
        if (project.start_year, project.start_month, project.start_day) >= (int(year), int(month), int(day)):
            print(f"{project}")


def add_new_project():
    """Adds new project using input"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost, percent_complete)


def update_project(projects):
    """updates one of the inputted projects"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    print(f"{projects[choice]}")
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    projects[choice].completion_percentage = new_percentage
    projects[choice].priority = new_priority


def main():
    my_projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("FileName: ")
            my_projects = load_file(filename)
        elif choice == "S":
            filename = input("FileName: ")
            save_to_file(filename, my_projects)
        elif choice == "D":
            display_projects(my_projects)
        elif choice == "F":
            date = input("Date (DD/MM/YYYY): ")
            display_filtered_projects(my_projects, date)
        elif choice == "A":
            my_projects.append(add_new_project())
        elif choice == "U":
            update_project(my_projects)
        else:
            print("Invalid choice, please try again.")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()

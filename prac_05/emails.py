email_directory = {}

while True:

    email = input('Email: ')
    if not email:
        break

    username = email.split('@')[0]  # Split email by '@' symbol to get username
    name_parts = username.split('.')  # Splitting usernames by '.' Split username to separate first and last name
    name = ' '.join(part.title() for part in name_parts)

    confirmation = input(f'Is your name {name}? (Y/n) ')
    if confirmation.lower() not in ['', 'y', 'yes']:
        name = input('Name: ')

    email_directory[email] = name

for email, name in email_directory.items():
    print(f'{name} ({email})')

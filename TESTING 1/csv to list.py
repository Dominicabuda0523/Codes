# Login function NEW

import csv

def Login(username, password):
    try:
        with open('Accounts_data.csv', 'r', encoding='utf8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader) # Skip the header row
            for row in csv_reader:
                un = str(row[0])
                pw = str(row[1])
                if username == un and password == pw:
                    print('Login successful.')
                    return True
            else:
                print('Login failed. Incorrect username or password.')
                return False
    except FileNotFoundError:
        print('File not found. Perhaps create a new one?')

def user_login():
    username = input('Username: ')
    password = input('Password: ')
    return Login(username, password)

user_login()
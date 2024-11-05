FILE_NAME = 'employees.csv'

def create_db():
    try:
        with open(FILE_NAME, 'w'):
            pass
    except:
        print('Cannot create the file')

def insert_new():
    try:
        with open(FILE_NAME, 'a') as f:
            while True:
                try:
                    id = int(input('ID: '))
                    if id == -1: break 
                    name = input('Name: ')
                    salary = float(input('Salary: '))
                    f.write(f'{id},{name},{salary}\n')
                except Exception as err:
                    print('Got an error:', err) 
    except Exception:
        print('Something is wrong with the file')

def display_all():
    try:
        with open(FILE_NAME, 'r') as f:
            print(f"{'id':8}{'name':15}{'salary':10}")
            for line in f:
                # 123,Jack,33.44\n
                fields = line.rstrip('\n').split(',')
                print(f'{fields[0]:8}{fields[1]:15}{fields[2]:10}')
    except Exception: # FileNotFoundError
        print('File not found')

def search():
    # get id, display name & salary
    try:
        with open(FILE_NAME, 'r') as f:
            key = int(input('Enter ID to search: '))
            line = f.readline()
            while line != '':
                id = int(line.rstrip('\n').split(',')[0])
                if id == key:
                    print(f"Found the guy, name is {line.split(',')[1]}" + f"His salary is {line.rstrip(' ').split(',')[2]}")
                    return 
                line = f.readline()
            print('Employee does not exist')
    except Exception as err:
        print('Error:', err)

def update():
    # way1: create a temp file, do update, delete original file, rename temp file
    # - import os, os.rename(), os.remove()
    # way2: read data to string, write new string to file
    content = ''
    try:
        with open(FILE_NAME, 'r') as f:
            to_change = int(input('Enter ID to update: '))
            for line in f:
                id = int(line.split(',')[0])
                if id == to_change:
                    name = input('Enter new name: ')
                    salary = float(input('Enter new salary: '))
                else:
                    name = line.split(',')[1]
                    salary = line.rstrip('\n').split(',')[2]
                content += f'{id},{name},{salary}\n'
        with open(FILE_NAME, 'w') as f:
            f.write(content)
    except Exception as err:
        print(err)

def delete():
    content = ''
    try:
        with open(FILE_NAME, 'r') as f:
            to_change = int(input('Enter ID to delete: '))
            for line in f:
                id = int(line.split(',')[0])
                if id == to_change:
                    continue
                else: # no need
                    name = line.split(',')[1]
                    salary = line.rstrip('\n').split(',')[2]
                    content += f'{id},{name},{salary}\n'
        with open(FILE_NAME, 'w') as f:
            f.write(content)
    except Exception as err:
        print(err)

def employee_mgmt_sys():
    # print menu, get choice
    while True:
        choice = input('0-Exit\n1-Create DB\n2-Insert\n3-Display\n4-Search\n5-Update\n6-Delete\nYour Choice:')
        if choice == '0': break
        create_db() if choice == '1' else \
        insert_new() if choice == '2' else \
        display_all() if choice == '3' else \
        search() if choice == '4' else \
        update() if choice == '5' else \
        delete() if choice == '6' else \
        print('Invalid choice')
 
def main():
    employee_mgmt_sys()

main()
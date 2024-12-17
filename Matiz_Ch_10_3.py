import json
# Функции json.dump() и json.load()
"""
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
with open(filename) as f:
    numbers = json.load(f)
print(numbers)
"""
# -------------------------------------
"""
username = input("What is your name? ")
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
"""
# -------------------------------------
"""
# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
"""
# -------------------------------------
"""
# Рефакторинг кода
def get_stored_username():
    ''' Получает хранимое имя пользователя, если оно существует '''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    ''' Запрашивает новое имя пользователя '''
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username;

def greet_user():
    ''' Приветствует пользователя по имени '''
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
"""
# -------------------------------------
"""
# HW 10.11
filename = 'favorite_number.json'
answer = input("What is your favorite number? ")
with open(filename, 'w') as f:
    json.dump(answer, f)
with open(filename) as f:
    number = json.load(f)
print(f"I know your favorite number! It is {number}")
"""
# -------------------------------------
# HW 10.12
filename = 'favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f"We'll remember your favorite number when you come back, {number}!")
else:
    print(f"Your favorite number is {number}!")
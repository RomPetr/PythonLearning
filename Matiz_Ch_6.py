"""
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
"""

"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"You just earned {new_points} points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
"""

"""
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
"""

"""
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x position: {alien_0['x_position']}")
alien_0['speed'] = 'fast'
# Пришелец перемещается вправо
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Пришелец двигается быстро
    x_increment = 3
# Новая позиция равна сумме старой позиции и приращивания
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
"""

"""
# Удаление пары ключ-значение
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
"""

"""
# Словарь с однотипными объектами
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
"""

"""
# использование метода get() если нет искомого ключа в словаре
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)
"""

"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
for k in alien_0.keys():
    key = k
    print(key)
point = alien_0.pop('points')
print(f"Popped key is '{key}' == {point}")
# del alien_0['color']
print(alien_0)
"""
# --------------------------------------
"""
# HW 6.1
human_0 = {'first_name': 'alex', 'last_name': 'corvin', 'age': '30', 'city': 'Denver'}
print(f"The first name of this human is {human_0['first_name'].title()}.")
print(f"The last name is {human_0['last_name'].title()}")
print(f"His age is {human_0['age']}.")
print(f"And he lives in {human_0['city']}.")
"""
# --------------------------------------
"""
# HW 6.2
friends = {'alex': 6, 'martin': 8, 'regina': 12, 'phill': 5, 'antony': 3}
for key, value in friends.items():
   print(f"My friend {key.title()} likes the number {value}")
"""
# --------------------------------------
"""
# HW 6.3
gollosary = {'concatination': 'Конкатенация строк — это операция соединения двух или более строк в одну.',
             'repo': 'Репозиторий — хранилище данных, которое можно сравнить с каталогом информации.',
             'framework': 'Фреймворк — программная платформа, которая упрощает разработку.',
             'open_source': 'Open Source — программное обеспечение с открытым исходным кодом.',
             'deep_learning': 'Deep learning — глубокое машинное обучение. Это вид вид машинного обучения, при котором'
                              ' многослойные нейросети самостоятельно обучаются на больших массивах данных.',
             }
print("Конкатенация:")
print(f"{gollosary['concatination']}\n")
print("Репозиторий:")
print(f"{gollosary['repo']}\n")
print("Фреймворк:")
print(f"{gollosary['framework']}\n")
print("Open Source:")
print(f"{gollosary['open_source']}\n")
print("Глубокое машинное обучение:")
print(f"{gollosary['deep_learning']}\n")
"""
# --------------------------------------
"""
# Перебор словаря
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
"""
# --------------------------------------
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
"""

"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print(favorite_languages.keys())
"""
# -------------------------------------
"""
# Перебор ключей словаря в определенном порядке (функция sorted())
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
"""
# -------------------------------------
"""
# Перебор всех значений в словаре (метод values())
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for langusge in favorite_languages.values():
    print(langusge.title())
"""

"""
# Извлечение только неповторяющихся значений из словаря через множество set()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'corey': 'ruby',
    'phil': 'python',
    }
print("The following languages have bee mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
"""
# -------------------------------------
"""
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite language are:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
"""
# -------------------------------------
"""
# HW 6.4
gollosary = {'concatination': 'Конкатенация строк — это операция соединения двух или более строк в одну.',
             'repo': 'Репозиторий — хранилище данных, которое можно сравнить с каталогом информации.',
             'framework': 'Фреймворк — программная платформа, которая упрощает разработку.',
             'open_source': 'Open Source — программное обеспечение с открытым исходным кодом.',
             'deep_learning': 'Deep learning — глубокое машинное обучение. Это вид вид машинного обучения, при котором'
                              ' многослойные нейросети самостоятельно обучаются на больших массивах данных.',
             }
for key, val in gollosary.items():
    print(f"\n{key.title()}:")
    print(f"\t{val}")
"""
# --------------------------------------
"""
# HW 6.5
rivers_1 = {'nile': 'egypt', 'angara': 'russia', 'senna': 'france'}
# for key, value in rivers_1.items():
#     print(f"\nThe {key.title()} runs through {value.title()}.")
# for key in rivers_1.keys():
#     print(key.title())
for value in rivers_1.values():
    print(value.title())
"""
# --------------------------------------
"""
# Список словарей
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
"""
# --------------------------------------
"""
# Создание пустого списка для хранения пришельцев
aliens = []
# Создание 30ти зеленых пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# print(aliens)
# print(f"Total number of alienss: {len(aliens)}")

# Изменение характеристик первых трех пришельцев
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Вывод первых 5ти пришельцев
for alien in aliens[ :5]:
     print(alien)
print("...")

# Вывод количества созданных пришельцев
print(f"Total number of aliens: {len(aliens)}.")
"""
# --------------------------------------
"""
# Список в словаре
# Сохранение информации о заказанной пицце
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# Описание заказа
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
"""
# -------------------------------------
"""
# Любимые языки программирования
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"\n{name.title()}'s favorite language are:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
"""
# -------------------------------------
"""
# Словарь в словаре
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princenton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
"""

"""
# HW 6.1
human_0 = {'first_name': 'alex', 'last_name': 'corvin', 'age': '30', 'city': 'Denver'}
print(f"The first name of this human is {human_0['first_name'].title()}.")
print(f"The last name is {human_0['last_name'].title()}")
print(f"His age is {human_0['age']}.")
print(f"And he lives in {human_0['city']}.")
"""

"""
# HW 6.7
human_0 = {'first_name': 'alex', 'last_name': 'corvin', 'age': 30, 'city': 'Denver'}
human_1 = {'first_name': 'bob', 'last_name': 'wilkins', 'age': 35, 'city': 'new york'}
human_2 = {'first_name': 'christina', 'last_name': 'storn', 'age': 22, 'city': 'huston'}

people = [human_0, human_1, human_2]
for human in people:
    # print(human)
    print("--------------------")
    for key, val in human.items():
        if type(val) == int:
            val = str(val)
        print(f"{key}: {val.title()}")
        # full_name = f"{key['first_name']} {key['last_name']}"
        # print(f"\nFull name: {full_name}")
        # print(f"{key}: {val}")
"""

# HW 6.8
piggy = {'type': 'pig', 'name': 'piggy', 'owner': 'bob', 'gender': 'female', 'age': 3}
lucky = {'type': 'dog', 'name': 'lucky', 'owner': 'alice', 'gender': 'male', 'age': 2}
robby = {'type': 'hamster', 'name': 'robby', 'owner': 'rick', 'gender': 'male', 'age': 1}
kitty = {'type': 'cat', 'name': 'kitty', 'owner': 'lusy', 'gender': 'female', 'age': 10}
pets = [piggy, lucky, robby, kitty]
i = 0

for pet in pets:
    print("--------------------")
    i += 1
    print(f"{i} pet is:")
    for key, val in pet.items():
        if type(val) == int:
            val = str(val)
        print(f"{key}: {val.title()}")
"""
# HW 6.10
friends = {'alex': [6], 'martin': [8, 10], 'regina': [12], 'phill': [3, 5, 7], 'antony': [2, 4, 8]}
for key, values in friends.items():
    if len(values) < 2:
        # print(' '.join(map(str, values)))
        print(f"My friend {key.title()} likes the number: {''.join(map(str, values))}")
    else:
        print(f"My friend {key.title()} likes the numbers: {', '.join(map(str, values))}")
"""

"""
# вывод чисел в одну строку без [] скобок
a = [1, 2, 3, 4, 5]
# Iterate over each element of list
for val in a:
    print(val, end=' ')
"""
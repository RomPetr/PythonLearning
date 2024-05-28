"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}."

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
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

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)
#--------------------------------------
# HW 6.1
human_0 = {'first_name': 'alex', 'last_name': 'corvin', 'age': '30', 'city': 'Denver'}
print(f"The first name of this human is {human_0['first_name'].title()}.")
print(f"The last name is {human_0['last_name'].title()}")
print(f"His age is {human_0['age']}.")
print(f"And he lives in {human_0['city']}.")
#--------------------------------------

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
#--------------------------------------
# Перебор словваря
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

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

# Извлечение только неповторяющихся значений из словаря
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
#--------------------------------------

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

#--------------------------------------
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
#--------------------------------------
# HW 6.5
rivers_1 = {'nile': 'egypt', 'angara': 'russia', 'senna': 'france'}
# for key, value in rivers_1.items():
#     print(f"\nThe {key.title()} runs through {value.title()}.")
# for key in rivers_1.keys():
#     print(key.title())
for value in rivers_1.values():
    print(value.title())
#--------------------------------------
"""
# Создание пустого списка для хранения пришельцев
aliens = []
# Создание 30ти зеленых пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

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
